n = int(input())
s = [0] * n
for i in range(n):
    s[i] = input()
dic = {}
ans = 0
for i in range(n):
    temp = 0
    for k in range(len(s[i])):
        temp ^= (1 << (ord(s[i][k]) - ord('a')))
    if temp in list(dic.keys()):
        ans = ans + dic[temp]
    for j in range(26):
        chk = temp
        chk ^= (1 << j)
        if chk in list(dic.keys()):
            ans = ans + dic[chk]
    if temp in list(dic.keys()):
        dic[temp] += 1
    else:
        dic[temp] = 1
print(ans)
