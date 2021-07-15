def scramble(string, array):
  return ''.join(c for _, c in sorted(zip(array, string)))
