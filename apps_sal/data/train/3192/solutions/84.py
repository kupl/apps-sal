def how_many_dalmatians(n):
  return ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", 
      "101 DALMATIONS!!!"][int(n>10) + int(n>50) + int(n==101)]
