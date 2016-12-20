import re
import orodja
regex=re.compile(
	r'},&quot;name&quot;:&quot;(?P<naslov>.*?)&quot.*?'
	r'&quot;blurb&quot;:&quot;(?P<povzetek>.*?)&quot.*?'
	r'&quot;goal&quot;:(?P<cilj>.*?)\.0,&quot;pledged&quot;:(?P<pridobljen_denar>.*?)\.\d,&quot;state&quot;:&quot;(?P<uspeh>.*?)&quot;.*?'
	r'&quot;country&quot;:&quot;(?P<drzava>\D*?)&quot.*?'
	r'&quot;backers_count&quot;:(?P<st_backerjev>.+?),&quot.*?'
	r'&quot;creator&quot;:{&quot;id&quot;:\d+?,&quot;name&quot;:&quot;(?P<avtor>.*?)&quot;.*?'
	r'&quot;category&quot;:{&quot;id&quot;:\d+?,&quot;name&quot;:&quot;(?P<kategorija>.*?)&quot;.*?'
	,
	flags=re.DOTALL
)




i=0
j=0

for datoteka in orodja.datoteke('strani_projektov/')[:110]:
	for ujemanje in re.finditer(r'window\.current_project(?P<iskanje>.*?)www\.kickstarter\.com/discover/categories',orodja.vsebina_datoteke(datoteka)):
		i+=1
		iskalni_niz = ujemanje.groupdict()['iskanje']
	for projekt in re.finditer(regex,iskalni_niz):
		j += 1
		print(projekt.groupdict())

print(i)
print(j)