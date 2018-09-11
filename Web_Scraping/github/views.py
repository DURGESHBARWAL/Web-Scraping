from django.shortcuts import render
from django.http import HttpResponse
import requests 
from bs4 import BeautifulSoup 

def home(request):
	URL = "https://github.com/DURGESHBARWAL?tab=repositories"
	r = requests.get(URL) 

	soup = BeautifulSoup(r.text, 'html.parser') 

	repos = []
	table = soup.find('ul', attrs = {'data-filterable-for':'your-repos-filter'}) 

	for row in table.find_all('li', attrs = {'itemprop':'owns'}): 
		repo = {}
		repo['name'] = row.find('div').find('h3').a.text
		p = row.find('p', attrs = {'itemprop' : 'description'})
		if p is not None:
			repo['desc'] = p.text
		else:
			repo['desc'] = None
		lang = row.find('div', attrs = {'class':'f6 text-gray mt-2'}).find('span', attrs = {'class':'mr-3'})
		if lang is not None:
			repo['lang'] = lang.text
		else:
			repo['lang'] = None
		repos.append(repo)
	return render(request, 'home.html', {'repos': repos})

