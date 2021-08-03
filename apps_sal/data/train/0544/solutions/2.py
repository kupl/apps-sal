# cook your dish here
t = int(input())
for e in range(t):
    n = int(input())
    s = input()
    ans = ''
    for i in range(0, n, 4):
        s2 = s[i] + s[i + 1] + s[i + 2] + s[i + 3]
        l = [chr(q) for q in range(97, 113)]
        for z in s2:
            if z == '0':
                l = l[0:int(len(l) / 2)]
            else:
                l = l[int(len(l) / 2):]
        ans = ans + l[0]
    print(ans)
