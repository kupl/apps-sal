def vowel_indices(word):
  word = word.lower()
    
  new_list = []
    
  vow = ['a', 'o', 'e', 'i', 'u', 'y']
  for x in range(len(word)):
      if word[x] in vow:
          new_list.append(x+1)
  return new_list
