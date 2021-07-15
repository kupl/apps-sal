def vowel_indices(word):
  n = 0
  a = []
  for i in word:
    n = n+1
    if i.lower() in ['a','e','i','o','u','y']:
      a.append(n)
  return a

