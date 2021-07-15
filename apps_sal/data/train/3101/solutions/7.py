def palindrome_pairs(words):
  return [[words.index(i),words.index(j)] for i in words for j in words if str(i)+str(j)==(str(i)+str(j))[::-1] and i!=j]
