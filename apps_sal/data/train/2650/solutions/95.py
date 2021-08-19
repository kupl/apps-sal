(n, l) = [int(x) for x in input().split()]
la = []
for i in range(n):
    la.append(str(input()))
la.sort()
print(''.join((str(x) for x in la)))
