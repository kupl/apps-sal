import math
import string
MOD = pow(10, 9) + 7
p = 23
for _ in range(int(input())):
    n, d = list(map(int, input().split()))
    number = [(d)] * (n)
    C = [0] * (n + n)
    s = len(C) - 1
    for j in range(n - 1, -1, -1):
        carry = 0
        shift = s
        for i in range(n - 1, -1, -1):
            m = number[i] * number[j]
            summ = m + C[shift] + carry
            num = summ % 10
            c = summ / 10
            C[shift] = num
            carry = c
            shift -= 1
        C[shift] = C[shift] + carry
        s -= 1
    jump = 0
    for i in range(len(C)):
        if C[i] == 0:
            jump += 1
        else:
            break
    C = C[jump:]
    ans = 0
    for i in range(len(C)):
        ans += (pow(p, i, MOD) * int(C[i])) % MOD
    print(ans % MOD)
