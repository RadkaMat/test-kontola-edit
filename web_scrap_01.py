from bs4 import BeautifulSoup
import csv

with open('/storage/emulated/0/Download/Výsledky-hlasování-za-územní-celky-výběr-obce-volby.cz.htm', 'r') as html_soubor:
	obsah = html_soubor.read()
	
	polevka = BeautifulSoup(obsah, 'lxml')
	#print(polevka.prettify()) kontrola html
	#hledany_tag = polevka.find('h5')
	#print(hledany_tag) najde jen jeden tag
	hledane_tagy = polevka.find_all('h3')
	#for tag in hledane_tagy:
		#print(tag.text)
	hledane_tagy2 = polevka.find_all('td', class_='overflow_name')
	
	for tag in hledane_tagy2:
		#print(tag.text)
		mesto_voleb = tag.text
		
with open("volby_mesta.csv","w") as f:
    wr = csv.writer(f,delimiter="\n")
	wr.writerow(hledane_tagy)
