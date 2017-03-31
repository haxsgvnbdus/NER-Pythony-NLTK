#!/usr/bin/ python
# -*- coding: utf-8 -*-
import tokenize
import sys, getopt, math, os.path


def main(argv):

	try:
		opts, args = getopt.getopt(argv,"f:")
    	except getopt.GetoptError:
        	sys.exit(2)	

    	for opt, arg in opts:
    		if opt == '-f':
        		if os.path.isfile(arg):
				input = open(arg, 'r')
				tokens = tokenize.tokenize(input.readline, handle_token)
				
	
def handle_token(type, token, (srow, scol), (erow, ecol), line):

	print "%d,%d-%d,%d:%s" % (srow, scol, erow, ecol, token)		#repr for tokens to see its type
	

if __name__ == "__main__":
    main(sys.argv[1:])
