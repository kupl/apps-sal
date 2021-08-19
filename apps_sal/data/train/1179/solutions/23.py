import math
t = int(input())
while t > 0:
    ans = 0
    n = int(input())
    total = n * (n + 1) >> 1
    if total & 1 == 0:
        pivot = math.floor((-1 + math.sqrt(1 + 4 * total)) / 2)
        ans += n - pivot
        if pivot * (pivot + 1) >> 1 == total >> 1:
            ans += math.factorial(pivot) // (math.factorial(pivot - 2) * 2)
            if n - pivot > 1:
                ans += math.factorial(n - pivot) // (math.factorial(n - pivot - 2) * 2)
    print(ans)
    t -= 1
