import nltk
import networkx as nx
from networkx.algorithms.link_analysis.pagerank_alg import pagerank
import re
import operator
from textblob import TextBlob



def decontract(text):
	replacements = [
		("n't", ' not'),
		("let's", 'let us'),
		("i'm", 'i am'),
		("'re", ' are'),
		("'s", ' us'),
		("'d", ' did'),
		("'ll", ' will')
	]

	for r in replacements:
		text = re.sub(r[0], r[1], text)
	return text

def preprocess(raw):
	blob = TextBlob(raw)
	return blob.noun_phrases

	# tokens = nltk.word_tokenize(raw)
	# return tokens

def create_graph(tokens, dist):
	graph = nx.Graph()

	for index, token in enumerate(tokens):
		for i in range(dist):
			try:
				graph.add_edge(token, tokens[index+i])
			except IndexError:
				pass

	return graph

with open('input.txt', 'r') as f:
	raw = f.read()

tokens = preprocess(raw)
graph = create_graph(tokens, 5)
pr = pagerank(graph)
print(sorted(pr.items(), key=operator.itemgetter(1), reverse=True)[:10])
