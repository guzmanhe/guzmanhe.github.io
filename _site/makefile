
SOURCES=$(wildcard _cv/*.md)
OBJECTS=$(patsubst _cv/%.md,_site/cv/%.pdf,$(SOURCES))

vpath %.pdf _site/cv/
vpath %.html _site/cv/

all: .site $(OBJECTS)
	echo $(SOURCES)

.site: $(SOURCES)
	bundle exec jekyll build
	touch .site

%.pdf: %.html 
	wkhtmltopdf  --print-media-type $< $@


