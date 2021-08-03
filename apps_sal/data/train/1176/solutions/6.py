t = int(input())
l = []
for i in range(t):
    s = str(input())
    le = len(s)
    if(le < 4):
        l.append("NO")
    elif(s[le - 1] == '0' and s[le - 2] == '0' and s[le - 3] == '0' and s[le - 4] == '1'):
        l.append("YES")
    else:
        l.append("NO")
for i in l:
    print(i)
