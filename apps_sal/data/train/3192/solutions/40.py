def how_many_dalmatians(n):
  respond = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]

  if n <= 10:
       return respond[0]
  elif n <= 50:
       return respond[1]
  elif n == 101:
       return respond[3]
  return respond[2]
