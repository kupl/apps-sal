from random import shuffle
import re

def scrambler(m):
    lst = list(m.group())
    shuffle(lst)
    return ''.join(lst)

def mix_words(s):
    if isinstance(s, str): return re.sub(r'(?<=\w)\w{2,}(?=\w)', scrambler, s)
