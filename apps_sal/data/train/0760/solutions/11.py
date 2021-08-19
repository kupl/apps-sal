from math import factorial as ff
from itertools import permutations as p
from itertools import combinations as cc
a = ff(4) % 10
author = 'biggy_bs'


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        (g, y, x) = egcd(b % a, a)
        return (g, x - b // a * y, y)


def modinv(a, m):
    (g, x, y) = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def factorialMod(n, modulus):
    ans = 1
    l = []
    if n <= modulus // 2:
        for i in range(1, n + 1):
            ans = ans * i % modulus
            l.append(ans)
    return l


def precomputation():
    nC2 = [0] * 100002
    nC3 = [0] * 100002
    nC4 = [0] * 100002
    for i in range(100002):
        if i >= 1:
            nC2[i] = i * (i - 1) / 2
        else:
            nC2[i] = 0
        if i >= 2:
            nC3[i] = i * (i - 1) * (i - 2) / 6
        else:
            nC3[i] = 0
        if i >= 3:
            nC4[i] = i * (i - 1) * (i - 2) * (i - 3) / 24
        else:
            nC4[i] = 0
    return (nC2, nC3, nC4)


def count_two(arr, mod):
    ans = 0
    for i in range(26):
        if arr[i] == 0:
            continue
        for j in range(i + 1, 26):
            if arr[j] == 0:
                continue
            ans = (ans + arr[i] * arr[j]) % mod
            ans = (ans + arr[i] * arr[j] % mod * (arr[i] - 1) % mod * (arr[j] - 1) % mod * modinv(4, mod) % mod) % mod
            for k in range(j + 1, 26):
                if arr[k] == 0:
                    continue
                ans = (ans + arr[i] * arr[j] % mod * arr[k] % mod * 2 % mod) % mod
                ans = (ans + arr[i] * arr[j] % mod * arr[k] % mod * (arr[i] - 1) % mod) % mod
                ans = (ans + arr[i] * arr[j] % mod * arr[k] % mod * (arr[j] - 1) % mod) % mod
                ans = (ans + arr[i] * arr[j] % mod * arr[k] % mod * (arr[k] - 1) % mod) % mod
                for l in range(k + 1, 26):
                    if arr[l] == 0:
                        continue
                    ans = (ans + arr[i] * arr[j] % mod * arr[k] % mod * arr[l] % mod * 3 % mod) % mod
    return ans


mod = 10 ** 9 + 7
fact = factorialMod(100002, mod)
pre = precomputation()
nC2 = pre[0]
nC3 = pre[1]
nC4 = pre[2]
f = [0] * 100002
t = eval(input())
dic = {}
while t > 0:
    t -= 1
    s = input()
    len_s = len(s)
    dic = {}
    arr = [0] * 26
    for i in s:
        try:
            dic[i] += 1
        except:
            dic[i] = 1
    for i in s:
        arr[ord(i) - 97] += 1
    answer_two = count_two(arr, mod)
    answer_two = (answer_two % mod + 1 % mod) % mod
    count_one = 0
    for i in range(26):
        try:
            qww = dic[chr(i + 97)] % mod
            for j in range(i + 1, 26):
                try:
                    count_one = (count_one % mod + qww * dic[chr(j + 97)] % mod) % mod
                except:
                    break
        except:
            break
    xxx = fact[len_s - 1] % mod
    for i in dic:
        xxx = xxx % mod * modinv(fact[dic[i] - 1] % mod, mod) % mod
    ans = xxx * xxx % mod
    zero = xxx
    one = xxx * count_one % mod % mod
    if len(dic) == len_s:
        aa = len_s - 2
        two = aa % mod * (aa + 1) % mod * (aa + 2) % mod * (3 * aa + 5) % mod * modinv(24, mod) % mod
    elif len(dic) == 2 and (dic[s[0]] == 1 or dic[s[0]] == len_s - 1 or dic[s[0]] == len_s):
        two = 0
    else:
        two = 1
    two = two % mod * xxx % mod
    answer_two = answer_two % mod * xxx % mod % mod
    ct = 0
    if len_s <= 3:
        print(0)
    else:
        print((ans - answer_two % mod) % mod)
