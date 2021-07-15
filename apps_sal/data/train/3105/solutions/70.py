def count_sheep(n):
  lista = []
  for numbers in range(n):
    numbers= numbers+1
    lista.append("{} sheep...".format(numbers))

  return "".join(lista)
