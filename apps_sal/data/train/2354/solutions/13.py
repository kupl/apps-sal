pas = input()
n = int(input())
l_letters = set()
r_letters = set()
ans = False
for i in range(n):
    j = input()
    l_letters.add(j[0])
    r_letters.add(j[1])
    if j == pas:
        ans = True
    if j[0] == pas[1]:
        if pas[0] in r_letters:
            ans = True
    if j[1] == pas[0]:
        if pas[1] in l_letters:
            ans = True
if ans:
    print('YES')
else:
    print('NO')
