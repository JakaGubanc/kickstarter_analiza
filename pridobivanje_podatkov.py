import re
import orodja

for stran in range(1,101):
	naslov_glavni = 'https://www.kickstarter.com/discover/advanced?&sort=most_funded'
	polni_naslov='{}&page={}'.format(naslov_glavni,stran)
	ime_datoteke = 'strani_seznamov_projektov/{:02}.html'.format(stran)
	orodja.shrani(polni_naslov,ime_datoteke)