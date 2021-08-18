from math import factorial as ff
from itertools import permutations as p
from itertools import combinations as cc
a = ff(4) % 10
author = 'biggy_bs'


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def factorialMod(n, modulus):
    ans = 1
    if n <= modulus // 2:
        for i in range(1, n + 1):
            ans = (ans * i) % modulus
    else:
        for i in range(1, modulus - n):
            ans = (ans * i) % modulus
        ans = modinv(ans, modulus)

        if n % 2 == 0:
            ans = -1 * ans + modulus
    return ans % modulus


mod = 10**9 + 7

t = eval(input())
dic = {}
while t > 0:
    t -= 1
    s = input()
    if len(s) <= 100:
        uy = ''
        for i in range(len(s)):
            uy += str(i)
        xxc = cc(uy, 2)
        rtt = []
        for i in xxc:
            rtt.append(i)
        a = []
        ans_ct = 0
        s = list(s)
        flag = 0
        lul = []
        for ii in rtt:
            temp1 = s[:]
            temp1[int(ii[0])], temp1[int(ii[1])] = temp1[int(ii[1])], temp1[int(ii[0])]
            lul.append(''.join(temp1))
            for jj in rtt:
                temp2 = temp1[:]
                temp2[int(jj[0])], temp2[int(jj[1])] = temp2[int(jj[1])], temp2[int(jj[0])]
                lul.append(''.join(temp2))
        ans_ct = len(set(lul))
        dic = {}
        for i in s:
            try:
                dic[i] += 1
            except:
                dic[i] = 1
        xxx = factorialMod(len(s), mod)
        for i in dic:
            xxx = (xxx % mod * modinv(factorialMod(dic[i], mod), mod)) % mod
        ans = (xxx * xxx) % mod
        ct = 0
        if len(s) <= 3:
            print(0)
        else:
            print((ans - (ans_ct * xxx) % mod) % mod)
