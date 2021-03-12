import argparse
import random
import sys

import wikipedia
from nltk.corpus import wordnet


def execute_from_command_line():
    parser = argparse.ArgumentParser(description='Translate text into gibberish')
    parser.add_argument('-s', '--string', dest='input_str', help='Directly pass a string')
    parser.add_argument('-t', '--txt', dest='txt_path', help='.txt file path')
    parser.add_argument('-w', '--wiki', dest='wiki_url', help='Wikipedia url')
    parser.add_argument('-o', '--out', dest='out',
                        help='If you want to store the result into some file, add the path here')

    args = parser.parse_args()

    with open('stopwords.txt', 'r') as f_in:
        stopwords = f_in.read().split('\n')

    text = __load_text(args)
    syn_text = __text_to_gibberish(text, stopwords)

    print(syn_text)


def __load_text(args):
    if args.input_str:
        return args.input_str
    elif args.txt_path:
        with open(args.txt_path, 'r') as f_in:
            return f_in.read()
    elif args.wiki_url:
        return wikipedia.summary(args.wiki_url)
    else:
        print("No valid input")
        sys.exit(0)


def __text_to_gibberish(text, stopwords):
    gibberish = ''

    for line in text.split('\n'):
        tokens = line.split()
        syns = []
        for token in tokens:
            prefix = ''
            suffix = ''

            if not token[0].isalpha():
                prefix = token[0]
                token = token[1:]
            if not token[-1].isalpha():
                suffix = token[-1]
                token = token[:-1]

            if token in stopwords:
                syns.append(prefix + token + suffix)
                continue

            if any(not char.isalpha() for char in token):
                syns.append(prefix + token + suffix)
                continue

            token_syns = wordnet.synsets(token.lower())
            if not token_syns:
                syns.append(prefix + token + suffix)
                continue

            syn = random.choice(token_syns)
            syn = syn.lemmas()[0].name()

            if token[0].isupper():
                syn = syn.capitalize()

            syn = syn.replace('_', ' ')
            syn = prefix + syn + suffix
            syns.append(syn)
        gibberish += ' '.join(syns) + '\n'

    return gibberish
