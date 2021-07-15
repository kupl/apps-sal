from functools import lru_cache

kases = int(input())
while kases > 0:
    kases = kases - 1
    T = int(input())
    arr = list(map(int, input().split(" ")))
    @lru_cache(maxsize=500)
    def ans(i, j):
        if i > j:
            return 0
        val = arr[i]
        x = i
        k = i
        while k <= j:
            if arr[k] > val:
                val = arr[k]
                x = k
            k = k + 1
        if x == i or x == j:
            return 1
        return 1 + min(ans(i, x - 1), ans(x + 1, j))
    print(ans(0, T - 1))


