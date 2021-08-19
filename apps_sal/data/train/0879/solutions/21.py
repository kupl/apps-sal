def sumOfLastDig(n, m):
    sum = 0
    k = n // m
    arr = [0] * 10
    for i in range(10):
        arr[i] = m * (i + 1) % 10
        sum += arr[i]
    rem = k % 10
    ans = k // 10 * sum
    for i in range(rem):
        ans += arr[i]
    return ans


def __starting_point():
    for i in range(int(input())):
        (m, n) = list(map(int, input().strip().split()))
        print(sumOfLastDig(m, n))


__starting_point()
