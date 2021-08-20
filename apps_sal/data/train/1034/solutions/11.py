def factorize(n):
    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            cntr = 0
            while n % i == 0:
                cntr += 1
                n //= i
            factors.append(i ** cntr)
    if n != 1:
        factors.append(n)
    return factors


def bruteForce(pos, arr, factors):
    if pos == len(factors):
        return sum(arr)
    ans = float('inf')
    for i in range(len(arr)):
        arr[i] *= factors[pos]
        ans = min(ans, bruteForce(pos + 1, arr, factors))
        arr[i] //= factors[pos]
    return ans


def __starting_point():
    t = int(input())
    while t != 0:
        (k, x) = list(map(int, input().split()))
        factors = factorize(x)
        lenn = len(factors)
        if lenn <= k:
            ans = sum(factors) + k - lenn
        else:
            arr = [1] * k
            ans = bruteForce(0, arr, factors)
        print(ans)
        t = t - 1


__starting_point()
