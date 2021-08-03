def how_many_dalmatians(n): return ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"][sum([n > 10, n > 50, n >= 101])]
