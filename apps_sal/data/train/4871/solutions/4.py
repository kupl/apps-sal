import re
from collections import Counter
def letter_frequency(text):
  letters = re.findall('[a-z]', text.lower())
  freqs   = Counter(letters).most_common()
  return sorted(freqs, lambda a, b: cmp(b[1], a[1]) or cmp(a[0], b[0]))
