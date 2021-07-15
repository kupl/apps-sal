def time(d, v, s):
     return round(d / (v + int(s.split()[1]) * ("D" in s or -1)), 2)
