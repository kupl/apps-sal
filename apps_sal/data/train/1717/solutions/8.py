from collections import Counter as C
from re import sub as s
from string import punctuation as p
def top_3_words(__):
    __ = s('[{}]'.format(p.replace("'",'')),' ',__).lower() 
    return list(filter(lambda c: c.replace("'",'').isalnum(),(_[0] for _ in C(__.split()).most_common(3))))
