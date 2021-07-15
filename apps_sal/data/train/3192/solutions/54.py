def how_many_dalmatians(n):
    d = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];
    # respond = if number <= 10 then dogs[0] else if (number <= 50 then dogs[1] else (number = 101  dogs[3] else dogs[2]
    return d[0] if n <= 10 else d[1] if n <= 50 else d[3] if n==101 else d[2]
