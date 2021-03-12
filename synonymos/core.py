import argparse
import os
import random

import wikipedia
from nltk.corpus import wordnet


def execute_from_command_line():
    parser = argparse.ArgumentParser(description='Translate text into gibberish')
    parser.add_argument('-s', '--string', dest='input_str', help='Directly pass a string')
    parser.add_argument('-t', '--txt', dest='txt_path', help='.txt file path')
    parser.add_argument('-w', '--wiki', dest='wiki_url', help='Wikipedia url')
    parser.add_argument('-o', '--out', dest='out',
                        help='If you want to store the result into some file, add the directory path here')

    args = parser.parse_args()

    __check_output_dir(args.out)

    with open('stopwords.txt', 'r') as f_in:
        stopwords = f_in.read().split('\n')

    text = __load_text(args)
    syn_text = __text_to_gibberish(text, stopwords)

    __store_or_print(syn_text, args.out)


def __check_output_dir(out_dir):
    if out_dir and not os.path.isdir(out_dir):
        raise OSError(f"{out_dir} does not exist...")


def __store_or_print(result, out_dir):
    if out_dir:
        with open(os.path.join(out_dir, 'syn.txt'), 'w') as f_out:
            f_out.write(result)
    else:
        print(result)


def __load_text(args):
    if args.input_str:
        return args.input_str
    elif args.txt_path:
        with open(args.txt_path, 'r') as f_in:
            return f_in.read()
    elif args.wiki_url:
        return wikipedia.summary(args.wiki_url)
    else:
        raise Exception("No valid input argument. Use `syn.py -h` for more information")


def __text_to_gibberish(text, stopwords):
    gibberish = ''

    for line in text.split('\n'):
        line_gibberish = __line_to_gibberish(line, stopwords)
        gibberish += line_gibberish + '\n'

    return gibberish


def __strip_token(token):
    prefix = ''
    suffix = ''

    if not token[0].isalpha():
        prefix = token[0]
        token = token[1:]
    if not token[-1].isalpha():
        suffix = token[-1]
        token = token[:-1]

    return prefix, token, suffix


def __line_to_gibberish(line, stopwords):
    syns = []

    for token in line.split():
        prefix, sub_token, suffix = __strip_token(token)

        if sub_token.lower() in stopwords or any(not char.isalpha() for char in sub_token):
            syns.append(token)
            continue

        token_syns = list(set(syn.lemmas()[0].name() for syn in wordnet.synsets(sub_token.lower())))

        if not token_syns:
            syns.append(token)
            continue

        syn = random.choice(token_syns)

        if sub_token[0].isupper():
            syn = syn.capitalize()

        syn = syn.replace('_', ' ')
        syn = prefix + syn + suffix
        syns.append(syn)

    return ' '.join(syns)
