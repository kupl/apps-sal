def how_many_dalmatians(n):
    a = ("Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!")
    return a[0] if n <= 10 else a[1] if n <= 50 else a[3] if n == 101 else a[2]
