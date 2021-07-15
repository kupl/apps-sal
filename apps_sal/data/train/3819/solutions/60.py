def smash(words):
  string = ''
  for i in range(len(words)):
      string += words[i] + ' '
  string = string[:-1]
  return string
