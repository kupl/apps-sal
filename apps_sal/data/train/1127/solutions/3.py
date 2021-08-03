t = int(input())
for i in range(t):
    s = input().split()
    res = ""
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    if(len(s) == 1):
        res = res + s[0]
    elif(len(s) == 2):
        k = s[0]
        res = res + k[0] + ". " + s[1]
    elif(len(s) == 3):
        l = s[0]
        m = s[1]
        res = res + l[0] + ". " + m[0] + ". " + s[2]
    print(res)
