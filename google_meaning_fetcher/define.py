#!/usr/bin/python2

import json
import urllib
import re
import binascii

def asciirepl(match):
  s = match.group()  
  return '\\u00' + match.group()[2:]

def get_meaning(query):
    p = urllib.urlopen('http://www.google.com/dictionary/json?callback=a&q='+query+'&sl=en&tl=en&restrict=pr,de&client=te')
    page = p.read()[2:-10] #As its returned as a function call
    
    #To replace hex characters with ascii characters
    p = re.compile(r'\\x(\w{2})')
    ascii_string = p.sub(asciirepl, page)

    #Now decoding cleaned json response
    data = json.loads(ascii_string)
    
    #Assumes that we always recieve a webDefinitions. ??Yet to check??
    if "webDefinitions" not in data:
        return None

    no_of_meanings = len(data['webDefinitions'][0]['entries']) 
    all_meanings = dict()
    all_meanings['primaries'] = dict()
    all_meanings['webDefinitions'] = list()

    if 'primaries' in data:
        #Creating list() for each types: adj, verb, noun
        for bunch in data['primaries']:
            #This list contains meanings and examples
            all_meanings['primaries'][bunch['terms'][0]['labels'][0]['text']] = list()
            means = all_meanings['primaries'][bunch['terms'][0]['labels'][0]['text']]
            
            for i in range(len(bunch['entries'])):
                #Choosen meaning, others can be related
                if bunch['entries'][i]['type'] != "meaning": continue
                meaning = bunch['entries'][i]['terms'][0]['text']
                try:    
                    example = list()
                    #Examples start with ZERO index
                    for i_ex in range(0, len(bunch['entries'][i]['entries'])):
                        example.append(bunch['entries'][i]['entries'][i_ex]['terms'][0]['text'])
                        
                except:
                    example = None
                means.append([meaning, example])
                
    #Web definitions
#    for meaning in data['webDefinitions'][0]['entries']:
#        all_meanings['webDefinitions'].append(meaning['terms'][0]['text'])
    
    return all_meanings
