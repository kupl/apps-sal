def how_many_dalmatians(n):
  
  #respond = if number <= 10 then dogs[0] else if (number <= 50 then dogs[1] else (number = 101  dogs[3] else dogs[2]
  if n == 101:
        return "101 DALMATIONS!!!"
  elif n < 11:
    return "Hardly any"
  elif n < 51:
        return "More than a handful!"
  else: 
    return "Woah that's a lot of dogs!"
