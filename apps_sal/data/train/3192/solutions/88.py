def how_many_dalmatians(n):
    msg = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    idx = {
        0: n <= 10,
        1: 10 < n <= 50,
        2: 50 < n <= 100,
        3: n >= 101
    }
    for k, v in idx.items():
        if v:
            return msg[k]
