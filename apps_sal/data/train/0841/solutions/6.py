t = int(input())
decimal = [1]
mod = 10 ** 9 + 7
for i in range(10 ** 5 + 1):
    decimal.append(decimal[-1] * 10 % mod)


def num(n):
    ans = 0
    length = len(n)
    for i in range(0, length):
        ans += int(n[i]) * decimal[length - i - 1] % mod
    return ans


for i in range(0, t):
    n = input()
    length = len(n)
    p = 10 ** length % mod
    p1 = 10 ** (length - 1) % mod
    mul = [1]
    for j in range(0, length - 1):
        mul.append(mul[-1] * p % mod)
    value = num(n)
    ans = 0
    for j in range(length - 1, -1, -1):
        temp = value * mul[j] % mod
        ans += temp
        value = value - int(n[length - 1 - j]) * p1
        value = (value * 10 + int(n[length - 1 - j])) % mod
    print(ans % mod)
