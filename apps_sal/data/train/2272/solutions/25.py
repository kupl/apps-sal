N = int(input())
A = [int(a) for a in input().split()]
B = [int(a) for a in input().split()]


def xor(L):
    a = 0
    for l in L:
        a ^= l
    return a


def chk(L1, L2, k):
    L1.sort()
    L2.sort()
    s, j = 0, 0
    for i in range(N)[::-1]:
        while j < N and L1[i] + L2[j] < k:
            j += 1
        s += N - j
    return s % 2 * k


t = (xor(A) ^ xor(B)) * (N % 2)
for i in range(28):
    m = 1 << i + 1
    t ^= chk([a % m for a in A], [b % m for b in B], m)

print(t)
