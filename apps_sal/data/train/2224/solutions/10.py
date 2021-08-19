n = int(input())
s1 = str(input())
s2 = str(input())
ans1 = 0
ans2 = 0
ans3 = 0
ans4 = 0
for i in range(n):
    if s2[i] == '0' and s1[i] == '1':
        ans1 += 1
    elif s2[i] == '0' and s1[i] == '0':
        ans2 += 1
    if s1[i] == '1':
        ans3 += 1
    if s1[i] == '0':
        ans4 += 1
ansx = 0
ansy = 0
for i in range(n):
    if s2[i] == '0' and s1[i] == '0':
        ansx += ans3 - ans1
        ansy += ans1
    elif s2[i] == '0' and s1[i] == '1':
        ansx += ans4 - ans2
        ansy += ans2
ans = ansx
ans += ansy // 2
print(ans)
