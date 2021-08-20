import sys
inf = float('inf')
(mod, MOD) = (1000000007, 998244353)


def get_array():
    return list(map(int, sys.stdin.readline().strip().split()))


def get_ints():
    return map(int, sys.stdin.readline().strip().split())


def input():
    return sys.stdin.readline().strip()


Arr = [0]
dp = [0]
prev_sum = 0
prev_length = 1
n = int(input())
while n:
    arr = get_array()
    if len(arr) == 2:
        number = arr[1]
        Arr.append(number)
        dp.append(0)
        ans = (prev_sum + number) / (prev_length + 1)
        print(ans)
        prev_length += 1
        prev_sum += number
    elif len(arr) == 3:
        (a, x) = (arr[1], arr[2])
        dp[a - 1] += x
        ans = (prev_sum + a * x) / prev_length
        print(ans)
        prev_sum += a * x
    else:
        ans = (prev_sum - (Arr[-1] + dp[-1])) / (prev_length - 1)
        print(ans)
        prev_sum -= Arr[-1] + dp[-1]
        prev_length -= 1
        dp[-2] += dp[-1]
        Arr.pop()
        dp.pop()
    n -= 1
