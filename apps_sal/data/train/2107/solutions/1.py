s = input()
res, n = 0, len(s)
for i in range(n - 1):
    j, c, q = i , 0, 0
    while (j < n):
        if(s[j] == '('):
            c += 1
        elif(s[j] == ')'):
            c -= 1
        else:
            q += 1
        if(c + q < 0):
            break
        if(c < q):
            c, q = q, c
        res += (c == q)
        j += 1
print(res)

