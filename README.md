Code for my website, at https://guzmanhe.github.io.
It is a fork from Adam Lopez's at https://alopez.github.io




#Generate papers

```

python scripts/parsebib.py papers/bibtex.bib  2>/dev/null  | perl -anpe 's/\t/    /g;' > _data/papers.yml

```

#Create individual pages for papers

```

python scripts/migrate.py _data/papers.yml  

```