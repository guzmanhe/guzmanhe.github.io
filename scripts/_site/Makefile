
SOURCES=cv/main.md
OBJECTS=$(SOURCES:.md=.html)
	
_site:
	bundle exec jekyll build

.html.pdf: _site
	wkhtmltopdf --print-media-type $< $@

clean:
	rm -f *.html *.pdf *.docx *.txt
