# cook your dish here
t = int(input())
for i in range(t):
    ans = 0
    n = int(input())
    a = [int(x) for x in input().split()]
    lis = sorted(a, reverse=True)
    for val in range(0, len(lis), 2):
        # print(val)
        ans = ans + lis[val]
    print(ans)
