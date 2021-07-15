# o(n) time, o(1) space
def two_sort(words):
  min_word = min(words)
  starred_word = "***".join(list(min_word))
  return starred_word
