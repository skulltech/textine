import nltk
import networkx as nx
import re


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

def preprocess(raw_text):
	tokens = nltk.word_tokenize(raw_text)
	return tokens

with open('input.txt', 'r') as f:
	raw = f.read()
