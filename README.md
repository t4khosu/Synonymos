# Synonymos
Mit dieser Software ist es möglich, Wörter von Texten englischer Sprache durch Synonyme zu ersetzen. Stop-Wörter werden dabei ignoriert!<br>
Es ist dabei möglich, als Eingabe eine eigene Datei vorzugeben oder einen Wiki-Artikel. Vom Wiki-Artikel werden N-Sätze der Summary verwendet.

## Setup
* `pip install -r requirements.txt`

## Eigene Texte
`python synonymos.py -s="test.txt"`
> Hello, how are you today?

> Welcome, how are you present-day?

## Wiki Texte
`python synonymos.py -s="Donald Trump" -w`
> Donald John Trump (born June 14, 1946) is the 45th and current president of the United States.
Before entering politics, he was a businessman and television personality.
Trump was born and raised in the New York City borough of Queens and received an economics degree from the Wharton School.

> Donald Wc Influence( inbred June 14, 1946) is the 45th and ruling president of the In Accord Circumstances.
Forward make an entrance hat in the ring, he was a baron and small screen disposition.
Lead was intrinsic and heightened in the Virgin York Civil community of Queen Dowager and collected an finance proportion from the Wharton Jail.

