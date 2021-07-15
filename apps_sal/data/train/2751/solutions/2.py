import re

def word_search(query, seq):
    return [w for w in seq if re.search(query, w, re.I)] or ['None']

