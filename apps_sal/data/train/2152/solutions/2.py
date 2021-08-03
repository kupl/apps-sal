import bisect
import sys
input = sys.stdin.readline


def make_prime_factors(n):
    """自然数nの素因数を列挙したリストを出力する
    計算量: O(sqrt(N))
    入出力例: 156 -> [2, 2, 3, 13]
    """
    prime_factors = []
    for k in range(2, int(n**0.5) + 1):
        while n % k == 0:
            prime_factors.append(k)
            n = n // k
    if n != 1:
        prime_factors.append(n)
    return prime_factors


n = int(input())
a = list(map(int, input().split()))

ruiseki = [0] * (n + 1)
for i in range(n):
    ruiseki[i + 1] = ruiseki[i] + a[i]

sum_a = 0
for i in range(n):
    sum_a += a[i]
li = make_prime_factors(sum_a)


def count(begin, end, num):
    # print(ruiseki[begin+1:end+1])
    # print(a[begin:end])
    res = 0
    l = bisect.bisect_left(ruiseki[begin + 1:end + 1], (ruiseki[begin + 1] + ruiseki[end] + 1) // 2)
    for i, num2 in enumerate(a[begin:end]):
        if num2 == 1:
            res += abs(i - l)
    return res


if sum_a == 1:
    print(-1)
    return

ans = 10**18
for num in li:
    tmp_ans = 0
    cnt = 0
    begin = 0
    end = 0
    while True:
        if end == n:
            break
        cnt += a[end]
        if cnt == num:
            tmp_ans += count(begin, end + 1, num)
            begin = end + 1
            end = begin
            cnt = 0
        else:
            end += 1
    ans = min(tmp_ans, ans)
print(ans)
