#! python
# -*- coding: utf-8 -*-

# Copyright (c) 2015 Francisco Guzman
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# This script takes a bibtex entry and transforms it into a jekyll post for easy inclusion in your site (papers). It prints the posts in stdout

# usage:
# python parsebib.py bibtex.bib

import sys
#print(sys.version)

import bibtexparser
from bibtexparser.bwriter import BibTexWriter

import re


#this is to fix some accents, add more at leisure.
def preprocess(text):
	#text=text.encode("utf8")
	text=text.replace(u'\\\'{a}',u'á')
	text=text.replace(u'{\\\'a}',u'á')
	text=text.replace(u'\\\'{i}',u"í")
	text=text.replace(u'\\\'{e}',u'é')
	text=text.replace(u'\\`{a}',u'à')
	text=text.replace('--', '-') 
	text = re.sub(r'\{(.*?)\}', r'\g<1>', text)
	return text

def parseauthors(text):
	final=[]

	authors=text.split(' and ')
	

	for author in authors:
		try:
			(last,first)= author.split(',')
		except:
			print author+ "------------------"

		final.append(""+first.strip()+" "+ last.strip())

	return ", ".join(final[0:-1])+ u", and "+ final[-1] 

def parse(bibfile):

	with open(bibfile) as bibtex_file:
		writer = BibTexWriter()
		bib_database = bibtexparser.load(bibtex_file)

		for entry in bib_database.entries:
			print "\t-"
			print "\t\tlayout: paper"
			print "\t\tpaper-type: "+ preprocess(entry["type"])
			print "\t\tyear: " + preprocess(entry["year"])
			print "\t\tselected: no"
			print "\t\ttitle: >\n\t\t\t"+preprocess(entry["title"])
			print "\t\tauthors: "+ parseauthors(preprocess(entry["author"])).encode('UTF8')
			print "\t\timg: "
			print "\t\tvenue: "
			if("pages" in entry.keys()):
				print "\t\tpages: "+preprocess(entry["pages"])
			if("booktitle" in entry.keys()):
				print "\t\tbooktitle: >\n\t\t\t"+preprocess(entry["booktitle"])
			if("journal" in entry.keys()):
				print "\t\tjournal: "+preprocess(entry["journal"])
			if("url" in entry.keys()):
				print "\t\tdoc-url: "+preprocess(entry["url"])
			else:
				print "\t\tdoc-url: "

			if("abstract" in entry.keys()):
				print "\t\tabstract: >\n\t\t\t" + preprocess(entry["abstract"]).encode('UTF8')

			print "\t\tbibtex: >\n\t\t\t"+ writer._entry_to_bibtex(entry).replace("\n","\n\t\t\t").encode('UTF8')

			#print "\t\tpublisher: "+preprocess(entry["publisher"])

def main(args):
	if len(args) >0:
		parse(args[0])
	else:
		parse("../papers/bibtex.bib")

if __name__ == '__main__':

	main(sys.argv[1:])

