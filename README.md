# Synonymos

If you have ever wanted to change a perfectly normal text into some gibberish, this tool is going to help you!
Pass a wiki article URL, string or some text file path as parameter and all non-stopwords will be switched with some random synonyms.
Since wiki articles can be quite long, only the summary will be "translated".

## Setup
* Python >= 3.8 
* Requirements: `pip install -r requirements.txt`

## Usage
**Handle a simple string**
```
python syn.py -s <text>
```

**Handle a .txt file** 
```shell script
python syn.py -t <file path>
```

**Handle a wikipedia entry** 
```shell script
python syn.py -w <wiki title>
```

**Set an output directory**
```shell script
python syn.py -s <some string> -o <output dir>
```
The output file will be called `.../syn.txt`

## An example of Wiki Texte

> Donald John Trump (born June 14, 1946) is the 45th and current president of the United States.
Before entering politics, he was a businessman and television personality.
Trump was born and raised in the New York City borough of Queens and received an economics degree from the Wharton School.

> Donald Wc Influence( inbred June 14, 1946) is the 45th and ruling president of the In Accord Circumstances.
Forward make an entrance hat in the ring, he was a baron and small screen disposition.
Lead was intrinsic and heightened in the Virgin York Civil community of Queen Dowager and collected an finance proportion from the Wharton Jail.

