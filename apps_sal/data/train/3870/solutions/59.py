def solve(word):
  #el primer paso de la función es darle la vuelta al string.Check
  reverse = ''
  reverse_nospace = []
  for char in range(len(word)-1, -1, -1):
    reverse += word[char] 
  for i in reverse:
    reverse_nospace.append(i)
  for i2 in reverse_nospace:
    if i2 == ' ':
      reverse_nospace.remove(i2)
  #el segundo paso buscar el index de los espacios, usare list comprehension [expression for item in list]
  char_list = []
  index = []
  for char in word:
    char_list.append(char)
  for idx, space in enumerate(char_list):
    if space == ' ':
      index.append(idx)

  #el tercero, hacer que coincidan los espacios
  final_string = ''
  for position in index:
    reverse_nospace.insert(position, ' ')
  final_string = ''.join(reverse_nospace)

  return final_string


