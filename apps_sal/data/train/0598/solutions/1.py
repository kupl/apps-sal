n, k = input().split()
n = int(n)
k = int(k)
a = list(int(x) for x in input().split())
if k == 0:
    print(" ".join(str(x) for x in a))
elif k % 2 == 0:
    m = max(a)
    a = [m - x for x in a]
    m = max(a)
    a = [m - x for x in a]
    print(" ".join(str(x) for x in a))
else:
    m = max(a)
    a = [m - x for x in a]
    print(" ".join(str(x) for x in a))
