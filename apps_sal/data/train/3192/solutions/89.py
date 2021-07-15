def how_many_dalmatians(number):
  dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];
  
  #respond = dogs[0] if number <= 10 else if (number <= 50 dogs[1] else (number = 101  dogs[3] else dogs[2]
  
  if number <= 10:
      return dogs[0]
  elif number <= 50:
      return dogs[1]
  elif number < 101:
      return dogs[2]
  else:
      return dogs[3]
  
  
#return respond

