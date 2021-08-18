l = input().split()
n = int(l[0])
q = int(l[1])
l = input().split()
li = [int(i) for i in l]
xori = 0
si = [0 for i in range(n)]
for i in range(n):
    si[i] = xori
    xori = xori ^ li[i]
si.append(xori)
fi = list(li)
fi.append(xori)
for you in range(q):
    q1 = int(input())
    print(si[q1 % (n + 1)])
