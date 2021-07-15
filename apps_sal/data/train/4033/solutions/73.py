def contamination(text, char):
  #Code here ;)
  #print(text[1])
  lt = list(text)
  for i in range(len(lt)):
      lt[i] = char
  return "".join(lt)
