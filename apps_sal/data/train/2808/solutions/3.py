def trans(c):
  v = ord(c) - ord('A')
  if ord(c) == ord(' '):
    return ' '
  elif ord(c) < ord('J'):
    return ''.join([str((v // 5) + 1 ), str((v % 5) + 1)])
  else:
    v -= 1
    return ''.join([str((v // 5) + 1), str((v % 5) + 1)])
    

def polybius(text):
    return ''.join(map(trans, text))
