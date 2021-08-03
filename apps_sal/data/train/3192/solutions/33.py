def how_many_dalmatians(n):
    dogs = ["Hardly any", "Woah that's a lot of dogs!", "More than a handful!", "101 DALMATIONS!!!"]
    return dogs[(n > 10) * ((n <= 50) + 2 * (n == 101) + 1)]
