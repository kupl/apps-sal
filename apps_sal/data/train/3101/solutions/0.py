def palindrome_pairs(w):
  return [[i, j] for i in range(len(w)) for j in range(len(w)) if str(w[i])+str(w[j])==(str(w[i])+str(w[j]))[::-1] and i!=j]
