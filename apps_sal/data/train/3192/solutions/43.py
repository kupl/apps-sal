'''def how_many_dalmatians(number):
  dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];
  
  respond = if number <= 10 then dogs[0] else if (number <= 50 then dogs[1] else (number = 101  dogs[3] else dogs[2]
  
return respond'''


def how_many_dalmatians(n):
    answers = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    respond = 3 if n == 101 else 2 if n > 50 else 1 if n > 10 else 0
    return answers[respond]
