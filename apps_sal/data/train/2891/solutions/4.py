def find_the_key(message, code):
  key = ''.join(str(c - 'abcdefghijklmnopqrstuvwxyz'.index(m) - 1) for m, c in zip(message, code))
  return int(next(key[0:i] for i in range(1, len(key)) if all(key[0:i].startswith(key[j:j+i]) for j in range(i, len(key), i))))
