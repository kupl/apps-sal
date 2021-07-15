def how_many_dalmatians(n):
  dogs= ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];
  if 1<n<11:
      return dogs[0]
  if 10<n<51:
      return dogs[1]
  if 51<n<101:
      return dogs[2]
  if n == 101:
      return dogs[3]

