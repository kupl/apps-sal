try:
    n = int(input())
    for i in range(n):
        m = int(input())
        l = list(map(int, input().split()))
        q = int(input())
        for j in range(q):
            a, b = list(map(int, input().split()))
            newlist = l[(a - 1):b]
            print(sum(newlist))
except e:
    pass
