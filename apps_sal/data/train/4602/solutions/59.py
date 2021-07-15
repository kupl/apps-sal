def is_anagram(word_o, test_o):
  is_anagram = True

  word = word_o.lower()
  test = test_o.lower()

  if (len(word) != len(test)):
    is_anagram = False

  alist = list(test.lower())
  pos1 = 0

  while pos1 < len(word) and is_anagram:
    pos2 = 0
    found = False
    while pos2 < len(alist) and not found:
      if word[pos1] == alist[pos2]:
        found = True
      else:
        pos2 = pos2 + 1

    if found:
      alist[pos2] = None
    else: 
      is_anagram = False
    
    pos1 = pos1 + 1

  return is_anagram
