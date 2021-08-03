testcases = int(input())
for i in range(testcases):
    n = int(input())
    x = [int(y) for y in input().split()]
    l = [0] * n
    for i in range(n):
        l[x[i]] += 1
    for i in range(n):
        if(l[i] > 0):
            print(i, end=" ")
        else:
            print(0, end=" ")
    print()
