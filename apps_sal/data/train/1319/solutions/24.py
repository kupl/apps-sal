citizens, visits = list(map(int, input().split()))
total = citizens + visits
l = []
for i in range(total):
    n = int(input())
    if n == -1:
        l.sort()
        print(l[-1])
        l[-1] = 0
    else:
        l.append(n)
