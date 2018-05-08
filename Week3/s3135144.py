import requests
import sys
import re

                
def print_answer(query):
	url = 'https://query.wikidata.org/sparql'
	data = requests.get(url, params={'query': query, 'format': 'json'}).json()
	flag = 0
	for item in data['results']['bindings']:
		flag = 1
		for var in item :
			print(item[var]['value'])
	return flag



def create_query(prop, entity):
	query = 'SELECT DISTINCT ?answerLabel WHERE{ wd:%s wdt:%s ?answer. SERVICE wikibase:label{ bd:serviceParam wikibase:language "en".}}' % (entity, prop)
	return query 


def create_and_fire_query(question):
	m = re.search('(.*) is the (.*) of (.*)', question)
	url = 'https://www.wikidata.org/w/api.php'
	paramsQ = {'action': 'wbsearchentities', 'language': 'en', 'format': 'json'}
	paramsP = {'action': 'wbsearchentities', 'language': 'en', 'format': 'json', 'type': 'property',}
	
	
	paramsQ['search'] = m.group(3)
	json = requests.get(url, paramsQ).json()
	
	
	for result in json['search']:
		q_id = format(result['id'])
		paramsP['search'] = m.group(2)
		json = requests.get(url, paramsP).json()
		for result in json['search']:
			p_id = format(result['id'])
			query = create_query(p_id, q_id)
			return print_answer(query)
				

def main(argv):
	questions = []
	questions.append('What is the capital of Belgium?')
	questions.append('What is the currency of France?')
	questions.append('What is the population of Leeuwarden?')
	questions.append('What is the timezone of Syria?')
	questions.append('What is the motto of South Africa?')
	questions.append('What is the internet domain of Antarctica?')
	questions.append('What is the area of Japan?')
	questions.append('What is the highest point of Jamaica?')
	questions.append('What is the length of Nile river?')
	questions.append('Who is the head of state of Russia?')
	
	for x in range(0, 10):
		print(questions[x])
	
	for line in sys.stdin:
		line = line.rstrip()
		if line.endswith('?') or line.endswith('.'):
			line = line[:-1]
		if create_and_fire_query(line) == 0:
			print("We could not find the answer")
		print("Ask another question.")


if __name__ == "__main__":
	main(sys.argv)
