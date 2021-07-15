import re

def hex_word_sum(s):
    s = s.translate(str.maketrans('OS','05'))
    return sum( int(x,16) for x in re.findall(r'\b[\dA-F]+\b', s))
