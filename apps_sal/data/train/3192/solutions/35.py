d=["Hardly any",
    "More than a handful!",
    "Woah that's a lot of dogs!",
    "101 DALMATIONS!!!"]
def how_many_dalmatians(n):
    return d[3] if n==101 else d[0] if n<=10 else d[1] if n<=50 else d[2] 
