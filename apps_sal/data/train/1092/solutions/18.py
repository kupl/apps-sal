# cook your dish here
for _ in range(int(input())):
    n, k, e, m = map(int, input().split())
    s = []
    for i in range(n - 1):
        a = [int(x) for x in input().split()]
        s.append(sum(a))
    s.sort(reverse=True)
    a = [int(x) for x in input().split()]
    c = s[k - 1] + 1 - sum(a)
    if(c > m):
        print("Impossible")
    else:
        if(c > 0):
            print(c)
        else:
            print(0)
