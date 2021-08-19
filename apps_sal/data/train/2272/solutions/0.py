#!/usr/bin/env python3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for k in range(30):
        C = [x & ((1 << (k + 1)) - 1) for x in A]
        D = [x & ((1 << (k + 1)) - 1) for x in B]
        C.sort()
        D.sort()
        # print(f'k = {k}')
        # print(f'C = {C}')
        # print(f'D = {D}')
        p, q, r = 0, 0, 0
        for i in range(N - 1, -1, -1):
            while p < N:
                if C[i] + D[p] >= 1 << k:
                    break
                p += 1
            while q < N:
                if C[i] + D[q] >= 2 << k:
                    break
                q += 1
            while r < N:
                if C[i] + D[r] >= 3 << k:
                    break
                r += 1
            x = ((q - p) + (N - r)) % 2
            # print(p, q, r, x)
            ans = ans ^ (x << k)
    print(ans)


main()
