def how_many_dalmatians(n):
    d=["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];
    return d[0] if n <= 10 else d[1] if n <= 50 else d[2] if n < 101 else d[3] 

