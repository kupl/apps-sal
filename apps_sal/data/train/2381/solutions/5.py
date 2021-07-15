t = int(input())
while t!=0:
    t-=1
    s=input()
    pos = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 'R':
            ans = max(ans, i-pos+1)
            pos = i+1
    ans = max(ans, len(s)+1-pos)
    print(ans)

