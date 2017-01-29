#!/bin/bash
export JEKYLL_ENV="local"
python scripts/migrate.py _data/papers.yml
bundle exec jekyll serve
