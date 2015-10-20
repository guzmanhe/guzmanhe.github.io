#!/bin/python
import simpleyaml as yaml
import codecs
# -*- coding: utf-8 -*-
from simpleyaml import Loader, SafeLoader


def main(file):
	stream = open(file, "r")
	docs = yaml.load(stream)
	for doc in docs:
		id=doc['img']
		
		newfile=open("../_papers/"+id+".html","w")
		#for item in doc.
		doc['layout']='singlepaper'
		doc['picture']='paco'
		string=yaml.dump(doc,explicit_start=True, default_flow_style=False,allow_unicode=True)
		newfile.write(string)
		newfile.write("---\n\n")
		newfile.write("{% include singlepaper.html paper=page %}")

		
		
		newfile.close()
		
		

if __name__ == '__main__':
	main("../_data/papers.yml")