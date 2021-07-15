def xor(a,b):
    c = 0
    n = str(a).count("True")
    m = str(b).count("True")
    c = n + m
    return (c%2)!=0
