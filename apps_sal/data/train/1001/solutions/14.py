# cook your dish here
bleh = int(input())
for i in range(bleh):
    n = int(input())
    l = list(map(int, input().split()))
    k = 0
    c = 0
    for j in range(n):
        k = 0
        if j < 5:
            for p in range(j):
                if l[j] >= l[p]:
                    k = 1
                    break
        else:
            for p in range(j - 5, j):
                if l[j] >= l[p]:
                    k = 1
                    break
        if k == 0:
            c = c + 1
    print(c)
