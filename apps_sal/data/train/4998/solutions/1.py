from collections import defaultdict
WORD_INDEX = defaultdict(list)
for w in WORD_LIST:
    WORD_INDEX[len(w), sum(map(w.count, 'aeiou'))].append(w)

def wanted_words(vowels, consonants, forbidden):
  return [w for w in WORD_INDEX[vowels + consonants, vowels] if not any(c in w for c in forbidden)]

