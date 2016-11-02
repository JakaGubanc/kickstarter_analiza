import re
import orodja

# for stran in range(1,151):
# 	naslov_glavni = 'https://www.kickstarter.com/discover/advanced?&sort=most_funded'
# 	polni_naslov='{}&page={}'.format(naslov_glavni,stran)
# 	ime_datoteke = 'strani_seznamov_projektov/{:02}.html'.format(stran)
# 	orodja.shrani(polni_naslov,ime_datoteke)

spletni_naslovi_projektov=set()
for datoteka in orodja.datoteke('strani_seznamov_projektov/'):
	naslovi_projektov=set()
	vsebina=orodja.vsebina_datoteke(datoteka)
	for naslov in re.finditer(r'<a href="/projects/(?P<spletni_naslov>.+)\?ref=most_funded" target=""',vsebina):
		spletni_naslovi_projektov.add(naslov.groupdict()['spletni_naslov'])


# stevec=1
# for naslov in spletni_naslovi_projektov:
# 	glavni_naslov='https://www.kickstarter.com/projects/'
# 	polni_naslov='{}{}'.format(glavni_naslov,naslov)
# 	ime_datoteke = 'strani_projektov/{:02}.html'.format(stevec)
# 	orodja.shrani(polni_naslov,ime_datoteke)
# 	stevec+=1

regex=re.compile(
	r'<a class="hero__link" href="/projects/.+?>(?P<naslov>.*?)</a>.*?'
	r'Created by.+?<a class="js-update-text-color" href="/projects/.+?>(?P<avtor>.*?)</a>.*?'
#	r'<span bind-event-blur="inlineEditExit(&#39;blurb&#39;)".+?blurb">(?P<opis>.*?)</span>.*?'
	r'<b>(?P<st_backerjev>.*?) backers</b>.*?'
#	r'location"></span>(?P<mesto>.*?), (?P<drzava>1.*?)</a>.*?'
#	r'icon__tag"></span>(?P<kategorija.*?>)</a>.*?'
	,
	flags=re.DOTALL

)
i=1
for datoteka in orodja.datoteke('strani_projektov/'):
	for projekt in re.finditer(regex,orodja.vsebina_datoteke(datoteka)):
		i+=1
		print(projekt.groupdict())


print(i)
