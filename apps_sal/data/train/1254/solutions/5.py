# cook your dish here
for t in range(int(input())):
    n, p = [int(x)for x in input().rstrip().split()]
    a = [int(x)for x in input().rstrip().split()]
    cakewalk = 0
    hard = 0
    for i in range(0, n):
        if a[i] >= p // 2 and a[i] <= p:
            cakewalk += 1
        elif a[i] >= 0 and a[i] <= p // 10:
            hard += 1
    if (cakewalk == 1 and hard == 2):
        print("yes")
    else:
        print("no")
