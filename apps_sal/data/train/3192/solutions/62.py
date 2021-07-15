def how_many_dalmatians(n):
 # dogs ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];
  
    if n <= 10: 
        return "Hardly any"
    elif n <= 50: 
        return "More than a handful!"
    elif n == 101: 
        return "101 DALMATIONS!!!"
    else: 
        return "Woah that's a lot of dogs!" 

