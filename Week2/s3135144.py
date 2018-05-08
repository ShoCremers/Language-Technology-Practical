import requests
import sys

def printAnswer(query):
	data = requests.get(url, params={'query': query, 'format': 'json'}).json()
	for item in data['results']['bindings']:
		print(data['results']['bindings'])
		if (len(item) > 1):
			for var in item :
				print(item[var]['value'], end = ' ')
			print()
		else:
			for var in item :
				print(item[var]['value'])

    
url = 'https://query.wikidata.org/sparql'



def main(argv):
	for line in sys.stdin:
		line = line.rstrip()
		question = int(line)
		
		if (question == 1):
			print("Which lake takes the water from Missouri river?")
    
			query='''SELECT ?lakeLabel

			WHERE{
			wd:Q5419 wdt:P469 ?lake .
			SERVICE wikibase:label {
			bd:serviceParam wikibase:language "en" .
			}

			}'''
			printAnswer(query)

		if (question==2):
			print("Which countries share the border with the Democratic Republic of the Congo?")
			query = '''SELECT ?countryLabel

			WHERE{
			wd:Q974 wdt:P47 ?country .
			SERVICE wikibase:label {
			bd:serviceParam wikibase:language "en" .
			}

			}'''
			printAnswer(query)

		if (question==3):
			print("How large is the city of Fukuoka?")
			query = '''SELECT ?areaLabel ?unitLabel

			WHERE{
			wd:Q26600 p:P2046 ?stmnode .
			?stmnode psn:P2046 ?valuenode .
			?valuenode wikibase:quantityAmount ?area .
			?valuenode wikibase:quantityUnit ?unit .
			SERVICE wikibase:label {
			bd:serviceParam wikibase:language "en" .
			}

			}'''
			printAnswer(query)

		if (question==4):
			print("State the height of the highest peak in Jamaica.")
			query = '''SELECT ?heightLabel ?unitLabel

			WHERE{
			wd:Q766 wdt:P610 ?name .
			?name p:P2044 ?stmnode .
			?stmnode psn:P2044 ?valuenode .
			?valuenode wikibase:quantityAmount ?height .
			?valuenode wikibase:quantityUnit ?unit .
			SERVICE wikibase:label {
			bd:serviceParam wikibase:language "en" .
			}

			}'''
			printAnswer(query)
    
		if (question==5):
			print("How many sister cities does Vancouver have?")
			query = '''SELECT (COUNT(?city) AS ?count)

WHERE{
  wd:Q24639 wdt:P190 ?city .
}'''
			printAnswer(query)
    
		if (question == 6):
			print("State the capital of Brazil before 1960.")
			query = '''SELECT ?cityLabel

WHERE{
  ?city p:P1376 ?statement .
  ?statement ps:P1376 wd:Q155 .
  ?statement pq:P580 ?time .
  FILTER(?time < "1960-01-01"^^xsd:dateTime )
  SERVICE wikibase:label {
     bd:serviceParam wikibase:language "en" .
  }

}'''
			printAnswer(query)
    
    
		if (question == 7):
			print("List the official languages of New Zealand.")
			query = '''SELECT ?languageLabel 

WHERE{
  wd:Q664 wdt:P37 ?language .
  SERVICE wikibase:label {
     bd:serviceParam wikibase:language "en" .
  }

}'''
			printAnswer(query)
    
    
		if (question == 8):
			print("Which state is Bangalore the capital of?")
			query = '''SELECT ?stateLabel 

WHERE{
  wd:Q1355 wdt:P1376 ?state .
  SERVICE wikibase:label {
     bd:serviceParam wikibase:language "en" .
  }

}'''
			printAnswer(query)
    
    
		if (question == 9):
			print("What is the population of Leeuwarden?")
			query = '''SELECT ?populationLabel 

WHERE{
  wd:Q25390 wdt:P1082 ?population .
  SERVICE wikibase:label {
     bd:serviceParam wikibase:language "en" .
  }

}'''
			printAnswer(query)
    
    
		if (question == 10):
			print("name the deepest point of Indian Ocean.")
			query = '''SELECT ?deepestPointLabel 

WHERE{
  wd:Q1239 wdt:P1589 ?deepestPoint .
  SERVICE wikibase:label {
     bd:serviceParam wikibase:language "en" .
  }

}'''
			printAnswer(query
			)
		
if __name__ == "__main__":
	main(sys.argv)
