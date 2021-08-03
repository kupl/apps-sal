def hex_to_dec(s):
    a = range(16)
    b = '0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F'.split(",")
    d = {j: i for i, j in zip(a, b)}
    v = sum(d[j.upper()] * (16**i) for i, j in enumerate(s[::-1]))
    return v
