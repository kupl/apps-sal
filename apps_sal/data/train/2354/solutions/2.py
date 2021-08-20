3
s = input()
n = int(input())
l = [input() for i in range(n)]
ans = False
if s in l:
    ans = True
else:
    for i in range(n):
        for j in range(n):
            if (l[i] + l[j])[1:3] == s:
                ans = True
if ans:
    print('YES')
else:
    print('NO')
