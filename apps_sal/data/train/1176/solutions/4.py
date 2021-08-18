t = int(input())
for i in range(t):
    s = str(input())
    n = len(s)
    if(n < 4):
        print("NO")
    elif(s[n - 4] != '0' and s[n - 3] == '0' and s[n - 2] == '0' and s[n - 1] == '0'):
        print("YES")
    else:
        print("NO")
