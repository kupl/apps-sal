def mod256_without_mod(number):
  a = abs(number)
  while a>256:
      a -= 256
  if number<0:
      b = 256-a
      return b
  elif a == 256: return 0
  else: return a
