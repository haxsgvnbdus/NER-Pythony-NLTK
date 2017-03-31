#!/usr/bin/ python
# -*- coding: utf-8 -*-
import re
import sys, getopt 


def main(argv):

	opts, args = getopt.getopt(argv,"f:")    	
    	for opt, arg in opts:
    		if opt == '-f':
			customize(open(arg, 'r'))
				
				
def customize(file):
	lines =  file.read().splitlines()
	isFirstLine = True
	pre_line = 0
	for each in lines:
		matches = re.match(r'(\d+),(\d+)-(\d+),(\d+):(.*)', each)
		if matches is not None:	 
			s = int(matches.group(2))										
			cur_line = int(matches.group(1))
			
			#this crap solves the several space crap 
			if cur_line > pre_line and s is not 0:
				e = int(matches.group(4))
				new_s = new_e
				new_e += e
				
			#3 cases 
			if not isFirstLine: 
				if int(matches.group(2)) == 0:
					e = int(matches.group(4))
					new_s = new_e
					new_e += e
				else:
					new_s = s - e + new_e 
					e = int(matches.group(4))
					new_e = e - s + new_s 
											
			else:	
				new_s = s		
				e = new_e = int(matches.group(4)) 
			
			#cleaning output: if this is words, print
			w = re.match(r'[^\s]', matches.group(5))
			if w is not None:
				fprint(matches.group(5), new_s, new_e)
			
			pre_line = int(matches.group(1))																
		

		isFirstLine = False


def fprint(word, start, end):
	print "%s\t%d->%d" % (word,start,end)
if __name__ == "__main__":
    main(sys.argv[1:])
