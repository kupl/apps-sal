try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(str(input()))[:n]
        i, c = 0, 0
        while(True):
            if(i >= len(s) - 1):
                break
            if(s[i] == s[i + 1]):
                c += 1
            i += 1
        print(c)
except:
    pass
