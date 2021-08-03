n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
m1 = 0
m2 = 0
for e in a:
    if (e > m1):
        m2 = m1
        m1 = e
    elif (e > m2 and e != m1):
        m2 = e
ans = 0
for e in a:
    temp = m1 % e
    if (temp > ans):
        ans = temp
print(max(m2 % m1, ans))
