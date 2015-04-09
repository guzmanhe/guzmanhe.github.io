#!/usr/bin/env python
# -*- coding: utf-8 -*-



import bibtexparser
from bibtexparser.bwriter import BibTexWriter

import re


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

with open('../papers/bibtex.bib') as bibtex_file:
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
			print "\t\tbooktitle: "+preprocess(entry["booktitle"])
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
