import re
n = int(input())
l = []
for _ in range(n):
    l.append(input().split())
    l[-1][1] = int(l[-1][1])

l.sort(key=lambda x: x[1], reverse=True)
q = int(input())
for _ in range(q):

    s = "^" + input()

    for k in l:
        if re.findall(s, k[0]):
            print(k[0])
            break
    else:
        print('NO')
