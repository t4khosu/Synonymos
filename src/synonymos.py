import argparse, sys, wikipedia, random, re, string, os
from nltk.corpus import stopwords
from nltk import word_tokenize
from thesaurus import Word
from tqdm import tqdm
from sentence_splitter import SentenceSplitter
from os.path import join

splitter = SentenceSplitter(language='en')
specialSymbols = re.compile(r"([.,!?])")

def getSynonyms(line):
	new_words = []
	stop_words = set(stopwords.words('english'))
	for word in tqdm(words):
		if word not in stop_words:
			try:
				w = Word(word)
				synonyms = w.synonyms()
				if synonyms:
					new_word = random.choice(synonyms)
					word = new_word.title() if word.istitle() else new_word
			except:
				pass
		new_words.append(word)
	return new_words
	

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Automatische Bestimmung von Synonymen')
	parser.add_argument('--source', '-s', help='Quelle der Daten order Titel eines Wiki-Artikels', required=True)
	parser.add_argument('--wiki', '-w', action='store_true', help='Quelle wird als Wikipedia-Link interpretiert')
	args = parser.parse_args()

	if(args.wiki):
		store_file = args.source + '_wiki_syn.txt'
		text = wikipedia.summary(args.source, sentences=3)
		lines = splitter.split(text=text)
	else:
		store_file = args.source + '_syn.txt'
		with open(args.source, 'r') as fIn:
			text = fIn.read().replace('\n', '')
			lines = splitter.split(text=text)
	if not lines:
		print('Data could not be loaded...')
		sys.exit(0)

	store_dir = '../results/'
	
	if not os.path.exists(store_dir):
		os.makedirs(store_dir)

	with open(join(store_dir, store_file), 'w', encoding='utf-8') as fOut:
		for line in lines:
			fOut.write(line + '\n')

		fOut.write('\n' + '='*100 + '\n\n')

		for line in lines:
			words = word_tokenize(line)
			words = getSynonyms(words)
			line = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in words]).strip()
			fOut.write(line + '\n')