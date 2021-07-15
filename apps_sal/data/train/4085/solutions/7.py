def mix_words(words):
  import re, random
  
  def slacrbme(word):
    mid = [c for c in word[1:-1]]
    random.shuffle(mid)
    return word[0] + ''.join(mid) + word[-1]
  
  return re.sub(r'(\w{3,})', lambda m: slacrbme(m.groups()[0]), words)
