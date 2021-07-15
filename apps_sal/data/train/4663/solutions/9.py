import re
def order(sentence):
  string_final = ''
  if sentence == '':
    return sentence
  lista = sentence.split()
  posicao=1
  while posicao <= len(lista):
    for i in range(len(lista)):
      if re.findall('\d+', lista[i]) == [str(posicao)]:
        string_final = string_final + lista[i] + ' '
        break
    posicao+=1
  return string_final[:-1]

