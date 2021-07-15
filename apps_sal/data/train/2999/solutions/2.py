def hex_word_sum(s):
  return sum(int(w, 16) for w in s.replace('O', '0').replace('S', '5').split() if all(c in '0123456789ABCDEF' for c in w))
