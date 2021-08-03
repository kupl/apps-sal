from collections import defaultdict
from itertools import filterfalse

is_vowel = set("aeiou").__contains__
result = defaultdict(lambda: defaultdict(list))
for w in WORD_LIST:
    nb_v = sum(map(is_vowel, w))
    nb_c = len(w) - nb_v
    result[nb_v][nb_c].append(w)


def wanted_words(n, m, forbid_let):
    return list(filterfalse(set(forbid_let).intersection, result.get(n, {}).get(m, [])))
