#!/usr/bin/env python
import sys

from itertools import groupby
from operator import itemgetter

class Reducer:
	def __init__(self, stream, sep = '\t'):
		self.stream = stream
		self.sep = sep

	def emit(self, k, v):
		sys.stdout.write("{0}{1}{2}\n".format(k, self.sep, v))

	def reduce(self):
		for word, group in groupby(self, itemgetter(0)):
			dict1={}
			for item in group:
				if item[1] not in dict1:
					dict1[item[1]]=1 #load value into dictionary if not present
				else:
					dict1[item[1]]+=1 #count if value alreadyexist	
			self.emit(word, dict1)

	def __iter__(self):
		for line in self.stream:
			w, val = line.split(self.sep)
			w = w.lower()
			yield w, val.split('\n')[0]

reducer = Reducer(sys.stdin)
reducer.reduce()
