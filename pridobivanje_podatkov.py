import re
import orodja

for stran in range(1,151):
	naslov_glavni = 'https://www.kickstarter.com/discover/advanced?&sort=most_funded'
	polni_naslov='{}&page={}'.format(naslov_glavni,stran)
	ime_datoteke = 'strani_seznamov_projektov/{:02}.html'.format(stran)
	orodja.shrani(polni_naslov,ime_datoteke)

spletni_naslovi_projektov=set()
for datoteka in orodja.datoteke('strani_seznamov_projektov/'):
	naslovi_projektov=set()
	vsebina=orodja.vsebina_datoteke(datoteka)
	for naslov in re.finditer(r'<a href="/projects/(?P<spletni_naslov>.+)\?ref=most_funded" target=""',vsebina):
		spletni_naslovi_projektov.add(naslov.groupdict()['spletni_naslov'])

print(spletni_naslovi_projektov)

stevec=1
for naslov in spletni_naslovi_projektov:
	glavni_naslov='https://www.kickstarter.com/projects/'
	polni_naslov='{}{}'.format(glavni_naslov,naslov)
	ime_datoteke = 'strani_projektov/{:02}.html'.format(stevec)
	orodja.shrani(polni_naslov,ime_datoteke)
	stevec+=1
