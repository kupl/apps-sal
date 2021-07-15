def reverse_list(l):
  'return a list with the reverse order of l'
  list = []
  for items in l: # Pour chaque "objet" dans la liste, on l'insert dans la nouvelle liste à la première position
      list.insert(0, items)
      print(list)
  return list
