#!/usr/bin/env python

import sys
import os
import string

SEP = "\t" #easy to change separator

class Mapper(object):

    	def __init__(self, stream, sep=SEP):
        	self.stream = stream
        	self.sep = SEP

    	def emit(self, key, value):
        	sys.stdout.write("{0}{1}{2}\n".format(key, self.sep, value))

    	def map(self):
		
		fn = os.getenv('map_input_file').split('/')[-1]
        	for line in self:
			for l in line.strip().split():			#split the word inside the file
				l=l.translate(None,string.punctuation)	#remove punctuations
				if len(l)>2:				#take avoid letters and single characters
					self.emit(l,fn)


	def __iter__(self):
        	for line in self.stream:
            		yield line

if __name__ == "__main__":
	mapper = Mapper(sys.stdin)
	mapper.map()

