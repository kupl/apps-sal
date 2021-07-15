def lower(e):
  return e.lower()

def sortme(words):
    words.sort(key=lower)
    return words
