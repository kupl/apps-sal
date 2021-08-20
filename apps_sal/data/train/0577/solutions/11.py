s = input()
n = int(input())
t = []
for _ in range(n):
    a = input()
    t.append(a)
for i in t:
    flag = True
    for j in i:
        if j not in s:
            flag = False
            break
    if flag:
        print('Yes')
    else:
        print('No')
