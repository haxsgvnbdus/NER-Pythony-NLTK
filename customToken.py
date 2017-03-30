import re
import sys, getopt, math, os.path


def main(argv):

	opts, args = getopt.getopt(argv,"f:")    	
    	for opt, arg in opts:
    		if opt == '-f':
			print "tokens file: " + arg 
			customize(open(arg, 'r'))
				
				
def customize(file):
	lines =  file.read().splitlines()
	isFirstLine = True
	
	for each in lines:
		matches = re.match(r'(\d+)-(\d+):(.*)', each)
		if matches is not None:		 
			s = int(matches.group(1))										
		
			if not isFirstLine: 
				if int(matches.group(1)) == 0:
					e = int(matches.group(2))
					new_s = new_e
					new_e += e
				else:
					new_s = s - e + new_e 
					e = int(matches.group(2))
					new_e = e - s + new_s 
											
			else:	
				new_s = s		
				e = new_e = int(matches.group(2)) 

			fprint(matches.group(3), new_s, new_e)																
		isFirstLine = False


def fprint(word, start, end):
	print "%s\t%d-%d" % (word,start,end)
if __name__ == "__main__":
    main(sys.argv[1:])