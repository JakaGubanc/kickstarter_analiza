import re
import orodja

for stran in range(1,101):
 	naslov_glavni = 'https://www.kickstarter.com/discover/advanced?&sort=end_date'
 	polni_naslov='{}&page={}'.format(naslov_glavni,stran)
 	ime_datoteke = 'strani_seznamov_projektov/{:02}.html'.format(stran)
 	orodja.shrani(polni_naslov,ime_datoteke)

spletni_naslovi_projektov=set()
for datoteka in orodja.datoteke('strani_seznamov_projektov/'):
	naslovi_projektov=set()
	vsebina=orodja.vsebina_datoteke(datoteka)
	for naslov in re.finditer(r'href="/projects/(?P<spletni_naslov>.+)\?.*?',vsebina):
		spletni_naslovi_projektov.add(naslov.groupdict()['spletni_naslov'])

print(spletni_naslovi_projektov)
print(len(spletni_naslovi_projektov))


with open('spletni_naslovi_projektov', 'w+') as datoteka:
	for naslov_projekta in spletni_naslovi_projektov:
		datoteka.write(naslov_projekta+'\n')

   

