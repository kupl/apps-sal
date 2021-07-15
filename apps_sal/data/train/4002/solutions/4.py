def memesorting(s):
    order_p,p,ini_p,order_c,c,int_c, order_d,d,int_d = {0: 'b', 1: 'u', 2: 'g'},"",0,{0: 'b', 1: 'o', 2: 'o', 3: 'm'},"",0,{0: 'e', 1: 'd', 2: 'i', 3: 't', 4: 's'},"",0
    for i in s.lower():
        if i == order_p[ini_p] : p += i ; ini_p += 1
        if i == order_c[int_c] : c += i ; int_c += 1
        if i == order_d[int_d] : d += i ; int_d += 1
        for k in range(3):
            if ["bug", "boom", "edits"][k] == [p, c, d][k] : return ["Roma", "Maxim", "Danik"][k]
    return "Vlad"
