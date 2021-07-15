def to_freud(sentence):
  words = sentence.split()
  wordscount = len(words)
  print(wordscount)
  s = ""
  while wordscount > 0:
      s = s + "sex "
      wordscount -= 1
  return s[:-1]
