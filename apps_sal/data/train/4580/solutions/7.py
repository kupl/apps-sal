tiaosheng = t = lambda a, e=0: a[0] + e + 3 > 60 and min(a[0], 60 - e) or t(a[1:], e + 3) if a else 60 - e
