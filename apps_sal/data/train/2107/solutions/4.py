st = input()
le = len(st)
ans = 0
for i in range(le):
    l = 0
    w = 0
    for j in range(i, le):
        if(st[j] == "("):
            l += 1
        elif(st[j] == ")"):
            l -= 1
        else:
            w += 1
        if(l + w < 0):
            break
        elif(w > l):
            xx = l
            l = w
            w = xx
        elif(l == w):
            ans += 1
print(ans)
