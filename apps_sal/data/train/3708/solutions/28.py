def hex_to_dec(s):
    
    dic = {'0123456789abcdef'[x] : x for x in range(16)}
    a = 0
    b = len(s) - 1
    c = 0
    
    while b >= 0 :
        a += dic[s[c]] * (16 ** b)
        b -= 1
        c += 1

    return a
