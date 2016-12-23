import re
import orodja
regex=re.compile(
	r'},&quot;name&quot;:&quot;(?P<naslov>.*?)&quot.*?'
	r'&quot;blurb&quot;:&quot;(?P<povzetek>.*?)&quot.*?'
	r'&quot;goal&quot;:(?P<cilj>.*?)\.0,&quot;pledged&quot;:(?P<pridobljen_denar>.*?)\.\d.*?'
	r'&quot;country&quot;:&quot;(?P<drzava>\D*?)&quot.*?'
	r'&quot;backers_count&quot;:(?P<st_backerjev>.+?),&quot.*?'
	r'&quot;creator&quot;:{&quot;id&quot;:\d+?,&quot;name&quot;:&quot;(?P<avtor>.*?)&quot;.*?'
	r'&quot;category&quot;:{&quot;id&quot;:\d+?,&quot;name&quot;:&quot;(?P<kategorija>.*?)&quot;.*?'
	,
	flags=re.DOTALL
)



projekti = []
for datoteka in orodja.datoteke('strani_projektov/'):
	for ujemanje in re.finditer(r'window\.current_project(?P<iskanje>.*?)www\.kickstarter\.com/discover/categories',orodja.vsebina_datoteke(datoteka)):
		iskalni_niz = ujemanje.groupdict()['iskanje']
	for projekt in re.finditer(regex,iskalni_niz):
		projekti.append(projekt.groupdict())




def pocisti_str(besedilo):
	besedilo = besedilo.replace(r'&#39;','\'')
	besedilo = besedilo.replace(r'&amp;','&')
	besedilo = besedilo.replace('\\\\n','')
	return(besedilo)

for projekt in projekti:
	projekt['cilj'] = int(projekt['cilj'])
	projekt['pridobljen_denar'] = int(projekt['pridobljen_denar'])
	projekt['st_backerjev'] = int(projekt['st_backerjev'])
	projekt['kategorija'] = pocisti_str(projekt['kategorija'])
	projekt['naslov'] = pocisti_str(projekt['naslov'])
	projekt['povzetek'] = pocisti_str(projekt['povzetek'])
	projekt['avtor'] = pocisti_str(projekt['avtor'])
	if projekt['pridobljen_denar'] < projekt['cilj']:
		projekt['uspesnost'] = 0
	else:
		projekt['uspesnost'] = 1


orodja.zapisi_tabelo(projekti,['naslov','avtor','drzava','kategorija','st_backerjev','cilj','pridobljen_denar','uspesnost','povzetek'],'projekti.csv')