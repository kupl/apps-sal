def factors(n):
    factor = []
    for i in range(2, int(n**(1 / 2)) + 1):
        cnt = 0
        if n % i == 0:
            while n % i == 0:
                cnt += 1
                n = n // i
            factor.append(i**cnt)
    if n != 1:
        factor.append(n)
    return factor


def bruteforce(pos, arr, factors):
    if pos == len(factors):
        return sum(arr)

    ans = float('inf')

    for i in range(len(arr)):
        arr[i] *= factors[pos]
        ans = min(ans, bruteforce(pos + 1, arr, factors))
        arr[i] //= factors[pos]
    return ans


for _ in range(int(input())):
    k, n = list(map(int, input().split()))
    fac = factors(n)
    if len(fac) == k:
        print(sum(fac))
    elif len(fac) < k:
        print(sum(fac) + k - len(fac))
    else:
        arr = [1] * k
        d = bruteforce(0, arr, fac)
        print(d)
