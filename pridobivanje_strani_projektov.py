import re
import orodja

spletni_naslovi_projektov=[]
with open('spletni_naslovi_projektov', 'r+') as datoteka:
	for vrstica in datoteka:
		spletni_naslovi_projektov.append(vrstica[:-1])

print(spletni_naslovi_projektov)

stevec=1
for naslov in spletni_naslovi_projektov:
 	glavni_naslov='https://www.kickstarter.com/projects/'
 	polni_naslov='{}{}'.format(glavni_naslov,naslov)
 	ime_datoteke = 'strani_projektov/{:05}.html'.format(stevec)
 	orodja.shrani(polni_naslov,ime_datoteke)
 	stevec+=1

