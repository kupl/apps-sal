t = eval(input())
while t != 0:
    md = {}
    t -= 1
    n = eval(input())
    wrds = input().split()
    c = 0
    for w in wrds:
        c += 1
        for i in range(len(w)):
            for j in range(i, len(w)):
                sub = w[i:j + 1]
                if sub not in md:
                    md[sub] = 1
                elif sub in md and md[sub] == c - 1:
                    md[sub] = c
    res = ""
    for k in list(md.keys()):
        if md[k] == n:
            if len(k) > len(res):
                res = k
            elif len(k) == len(res) and k < res:
                res = k
    print(res)
