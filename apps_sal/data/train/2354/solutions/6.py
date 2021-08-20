p = input()
n = int(input())
c = False
w = [input() for i in range(n)]
for i in range(n):
    for j in range(n):
        if w[i][0] == p[1] and w[j][1] == p[0]:
            c = True
            break
print({True: 'YES', False: 'NO'}[c or p in w])
