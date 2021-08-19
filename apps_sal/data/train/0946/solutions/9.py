# nexus01
n, k = input().split()
n, k = int(n), int(k)
test = n
slist = []
sumlist = []
while test:
    test -= 1
    sum = 0
    x = [float(a) for a in input().strip().split(' ')]
    slist.append(x)
    for a in x:
        sum += a
    sumlist.append(sum)

for c in range(0, k):
    prob = 0
    base = 1
    for i in range(0, n):
        if i == n - 1:
            base *= sumlist[n - i - 1]
        else:
            base *= (sumlist[n - i - 1] + 1)
        prob += (slist[n - i - 1][c] / base)
    print(prob, end=' ')
