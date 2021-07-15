def reverse_list(l):
  tmp = list.copy(l)
  counter = 0
  listIndex = len(tmp) - 1
  for i in l:
      l[counter] = tmp[listIndex]
      counter += 1
      listIndex -= 1
  return l
