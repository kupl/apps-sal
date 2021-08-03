import math


def main():
    while True:
        n, m, x = map(int, (input().split()))
        # print("n, m, x = ", n, m, x)

        if(n == 0 and m == 0 and x == 0):
            break

        k = int(1)
        l = int(0)
        r = int(0)

        ans = 0
        while True:
            l = (m * k - x + n - 1) // n
            l = int(l)
            r = (m * (k + 1) - x + n - 1) // n
            r -= 1
            r = int(r)
            # print("l, r, k = ", l, r, k)
            if l >= m:
                break
            if l < 0:
                l = 0
            if r >= m:
                r = m - 1
            if l > r:
                k += 1
                continue
            # print("Adding to answer")
            ans += (r - l + 1) * k
            k += 1
        ans = int(ans)
        print(str(ans))


main()
