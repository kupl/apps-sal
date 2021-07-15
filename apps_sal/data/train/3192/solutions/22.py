def how_many_dalmatians(n):
    n = int(n)
    if n <= 10:
       return "Hardly any"
    elif n <= 50:
        return "More than a handful!"
    elif n <= 100:
        return "Woah that's a lot of dogs!"
    elif n == 101:
        return "101 DALMATIONS!!!"
