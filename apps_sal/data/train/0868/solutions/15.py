import bisect
import math
t = int(input())
while t > 0:
    fp = 0
    (n, k) = map(int, input().split())
    a = [int(o) for o in input().split()]
    for i in range(n):
        left = []
        arr = [0] * 2050
        for j in range(i, n):
            right = a[j]
            bisect.insort(left, right)
            arr[a[j]] += 1
            uhoy = math.ceil(k / (j - i + 1))
            mc = int(math.ceil(k / uhoy))
            kpop = arr[left[mc - 1]]
            if arr[kpop] >= 1:
                fp += 1
    print(fp)
    t -= 1
