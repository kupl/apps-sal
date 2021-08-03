def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    return dogs[(n == 101) + (50 < n <= 101) + (n > 10)]
