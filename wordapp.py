#!/usr/bin/python
#author: Arpit Agarwal (arpit8991@gmail.com)
import string
from os import system
import sys
from random import *

system('clear')
tolearn=sys.argv[1:]


if len(tolearn) == 0:
	print 'No word data loaded\nUsage Example : appyapp c1 c2'

def meaningsword(mainlist):
	print '\n\nWrite the meanings for the following (enter q to quit in between): '
	
	wrongs=[]
	correct=0
	count =0
	shufflelist=mainlist
	shuffle(shufflelist)
	
	for pair in shufflelist:
		count += 1
		word = pair[0]
		meaning = pair[1]
		print '[',count,']\n'
		wordentered = raw_input('\t'+meaning+'  :  '+'-'*len(word)+'\b'*len(word))
		print ''
		if wordentered == word:
			print 'Correct!' 
			correct+=1

		elif wordentered == 'w':
			revisewrong(wrongs)
			
		elif wordentered == 'q':
			count-=1
			break
		else:
			print "Incorrect"
			print 'Ans : ',word
			wrongs.append(pair)
		dump=raw_input('-----------------------------------------------------------------------\n--press Enter to continue--')
		system('clear')

	print 'Your result : \n\nCorrect',correct,'/',count
	if len(wrongs):
		print 'Incorrect Words: \n',wrongs
		print "\n\nEnter 'yes' to revise the incorrect words : "
		ch = raw_input('');
		if ch == 'yes':
			print meaningsword(wrongs)
	else:
		print 'Congratulations all correct!'


def wordquiz(mainlist, wlist, mlist):
	shufflelist=mainlist
	shuffle(shufflelist)
	total = len(shufflelist)
	count = 0 
	correct = 0
	wrongs = []
	for pair in shufflelist:
		count+=1
		options = []
		word=pair[0]
		meaning = pair[1]
		tmlist=[]
		tmlist+=mlist
		mindex = tmlist.index(meaning)
		tmlist.pop(mindex)
		#print word, meaning, '\n',tmlist
		#print len(tmlist),' ',len(mlist),' range: ',range(total-2)
		samples=sample(range(total-2),4)
		print 'sammples: ',samples,'\n'
		for num in samples:
			options.append(tmlist[num])
		options.append(meaning)
		shuffle(options)
		correctans = options.index(meaning)+1
		dump=system("clear")
		print '[',count,'/',total,']\n'
		#print len(mlist),' ',total
		print '\t',word,'\n'
		i=0
		for m in options:
			i+=1
			print '[ ',i,' ]   ',m
		try:
			ans=int(input('\nEnter your answer (1-5): -\b'))
		except:
			ans=int(input('\nEnter your answer (1-5): -\b'))
			
		print '--------------------------------------------------------------\n'
		if ans==correctans:
			print 'Correct!'
			correct+=1
		else:	
			wrongs.append(pair)
			print 'Incorrect!'	
			print 'Ans :\t[ ',correctans,' ]',meaning
			
		print '--------------------------------------------------------------\npress enter to continue'
		dump = raw_input('')
	print 'Result : '
	print '\tcorrect :  ',correct,'/',count

def flasher(mainlist):
	system('clear')
	print '\n\n\tThe words you selected in the set will be displayed as flashcards, try to recall their meaning'
#	print '\nKeybindings:'
#	print 'Enter\tDisplay next word'
#	print 'r\tGoto next word and REPEAT the current word later'
	print '\n(Press ENTER to start)\n'
	shufflelist=mainlist
	a=shuffle(shufflelist) 
#	print shufflelist
	raw_input('')
	total=len(shufflelist)
	count=1
	for wordpair in shufflelist:
		system('clear')
		#mainlist.remove(wordpair)
		remaining=total-count
		print 'Progress:'+' ['+str(count)+'/'+str(total)+']\t[' +' '*count+'>=>O'+' '*remaining +']'
#		print shufflelist
		count=count+1
		print '\n----------------------------------------------------------------------------\n\n\t\t',wordpair[0].upper(),'\n\n----------------------------------------------------------------------------'
		dump=raw_input('')
		print '\n\t',wordpair[1]
		val=raw_input('')
	

wlist=[]
mlist=[]
llist=[]

mainlist=[]

for fil in tolearn:
	outfile= 'google_meaning_fetcher/'+fil
	fil = 'data/'+fil
	f=open(fil)
	fout=open(outfile,'w')
	llist=f.readlines()
	for line in llist:
		line=line.rstrip('\n')
		pair=line.split(' : ')
		mainlist.append(pair)
		wlist.append(pair[0])
		mlist.append(pair[1])
		fout.write(pair[0]+'\n')
	fout.close()

print '\nLoaded ',len(mainlist),'words'

ch = raw_input('\nEnter "ok" to print the list of all words, else press "enter" to skip : ') 
if ch == 'ok':
	print 'WORD','\t\t','MEANING'
	print '----\t\t-------'

	for pair in mainlist:
		print pair[0],'\t\t',pair[1]
		
else:
	print "Skipped"

dump =raw_input('')
dump=system('clear')

print "\n\tWORDAPP MENU\n"
print "1. Meanings to the words "
print "2. Word Meanings mcq "
print "3. Flash Words"
print "4. Exit"
ch=int(input("Enter Your choice (1-3) :  "))
if ch == 1:
	meaningsword(mainlist)
elif ch ==2:
	wordquiz(mainlist,wlist,mlist)
elif ch == 3:
	flasher(mainlist)
