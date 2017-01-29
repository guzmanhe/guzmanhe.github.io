
BIBLIO=$1
years=$(cat $BIBLIO | grep \@ | grep "$year" | cut -f2  -d \{ | sort -k2nr -t: | cut -f1 -d, | cut -f2 -d: | sort | uniq)


for year in $years 
do
echo "--- 
nocite: |" > $year.bib.md
cat $BIBLIO | grep \@ | grep "$year" | cut -f2  -d \{ | sort -k2nr -t: | cut -f1 -d, | awk '{ print "@"$1} ' \
| paste -d\; -s - | awk '{ print " ["$0"] "}'>> $year.bib.md
echo "
...">> $year.bib.md
#echo "###$year" >>$year.bib.md

done
