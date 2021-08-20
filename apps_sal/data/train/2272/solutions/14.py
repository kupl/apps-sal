import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def sorting(X, l):
    eX = []
    oX = []
    for x in X:
        if x & 1 << l:
            oX.append(x)
        else:
            eX.append(x)
    return eX + oX


ans = 0
for shift in range(30):
    A = sorting(A, shift)
    B = sorting(B, shift)
    div = 1 << shift + 1
    count = 0
    l1 = N
    r1 = N
    l2 = N
    r2 = N
    for a in A:
        while a % div + B[l1 - 1] % div >= div // 2 and l1 > 0:
            l1 -= 1
        while a % div + B[r1 - 1] % div >= div and r1 > 0:
            r1 -= 1
        while a % div + B[l2 - 1] % div >= div // 2 * 3 and l2 > 0:
            l2 -= 1
        while a % div + B[r2 - 1] % div >= 2 * div and r2 > 0:
            r2 -= 1
        count += r1 - l1 + (r2 - l2)
    if count % 2 == 1:
        ans += 1 << shift
print(ans)
