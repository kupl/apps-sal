def how_many_dalmatians(n):
  dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]

  
  if n <= 10:
      ans = dogs[0]
  elif n <= 50:
      ans = dogs[1]
  elif n == 101:
      ans = dogs[3]
  else:
      ans = dogs[2]
  return ans
