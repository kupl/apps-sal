import collections

def char_freq(message):
  return collections.Counter(message)
  


import collections
def char_freq(message):
  letters = collections.defaultdict(int)
  for letter in message:
    letters[letter] += 1
  return letters

