import random
tc = int(input())
while tc:
    graph1 = []
    graph2 = []
    n = int(input())
    for i in range(n):
        graph1.append([int(x) for x in input().split()])
    for i in range(n):
        graph2.append([int(x) for x in input().split()])
    for x in range(2):
        a = []
        op = ''
        for i in range(n):
            a.append(i + 1)
        k = n - 1
        while k:
            index = random.randint(0, k - 1)
            op += str(a[index]) + ' '
            a.pop(index)
            k -= 1
        op += str(a[0])
        print(op)
    tc -= 1
