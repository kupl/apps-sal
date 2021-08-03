testcases = int(input())
for i in range(testcases):
    x, y = [int(y) for y in input().split()]
    if(x % 2 == 0):
        print((x // 2) * y)
    else:
        print((x // 2 + 1) * y)
