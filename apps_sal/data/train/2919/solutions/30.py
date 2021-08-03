def encode(message, key):

    abc = "a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z".split("  ")
    cypher = []
    key = str(key)
    for i, letter in enumerate(list(message)):
        letterToDigit = abc.index(letter) + 1
        addedKeyIndex = i % len(key)
        addedKeyValue = key[addedKeyIndex]
        cypher.append(letterToDigit + int(addedKeyValue))
    return cypher
