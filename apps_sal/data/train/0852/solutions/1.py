from sys import*
input = stdin.readline
t = int(input())
for _ in range(t):
    k = int(input())
    l = [0 for _ in range(k)]
    for i in range(1, k):
        if l[i - 1] == 0:
            l[i] = 1
        else:
            l[i] = 0
    ans = "".join([str(x) for x in l])
    l1 = [1 for _ in range(k)]
    for i in range(1, k):
        if l1[i - 1] == 1:
            l1[i] = 0
        else:
            l1[i] = 1
    ans1 = "".join([str(x) for x in l1])
    for i in range(k):
        if (i % 2) == 0:
            print(ans)
        else:
            print(ans1)
