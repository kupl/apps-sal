d = [('H', 50), ('Q', 25), ('D', 10), ('N', 5), ('P', 1)]
make_change = lambda m, i=0, cng=[]: make_change(*([m % d[i][1], i + 1, cng + [(d[i][0], m // d[i][1])]] if m >= d[i][1] else [m, i + 1, cng])) if m else dict(cng)
'cng = {}\nfor i,j in d.items():\n        if money>=j:\n            cng[i] = money//j\n            money %= j\nreturn cng'
