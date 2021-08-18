from math import log10
import math
for _ in range(int(input())):
    n = int(input())
    alice = []
    bob = []
    words = []
    for i in range(n):
        words.append(input())
    for cur in words:
        prev = -1
        f = 0
        for j in range(len(cur)):
            if cur[j] not in ['a', 'e', 'i', 'o', 'u']:
                if prev == -1:
                    prev = j
                else:
                    if abs(prev - j) == 2 or abs(prev - j) == 1:
                        f = 1
                        break
                    else:
                        prev = j
        if f == 1:
            bob.append(cur)
        else:
            alice.append(cur)

    n1 = len(alice)
    freq_a = {}
    for i in alice:
        for j in i:
            if j not in freq_a:
                freq_a[j] = 1
            else:
                freq_a[j] += 1
    num_a = {}
    for i in freq_a:
        num_a[i] = 0
        for j in alice:
            if i in j:
                num_a[i] += 1
    num1 = 1
    den1 = 1
    for i in num_a:
        num1 = (num1 * num_a[i])
        den1 = den1 * freq_a[i]

    n2 = len(bob)
    freq_b = {}
    for i in bob:
        for j in i:
            if j not in freq_b:
                freq_b[j] = 1
            else:
                freq_b[j] += 1
    num_b = {}
    for i in freq_b:
        num_b[i] = 0
        for j in bob:
            if i in j:
                num_b[i] += 1
    num2 = 1
    den2 = 1
    for i in num_b:
        num2 = (num2 * num_b[i])
        den2 = den2 * freq_b[i]
    if n <= 10:
        ans1 = log10(num1) + n2 * log10(den2)
        ans2 = log10(num2) + n1 * (log10(den1))
        ans1 = ans1 - ans2
        if ans1 > 7.0:
            print("Infinity")
        else:
            print(pow(10, ans1))
