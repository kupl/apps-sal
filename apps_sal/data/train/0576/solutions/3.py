try:
    t = int(input())
    for _ in range(t):
        s = input()
        acount = 0
        for i in s:
            if i == "a":
                acount+=1
        p = len(s) - acount
        base = 2**(acount) - 1
        print(base * 2**(p))
except:
    pass
