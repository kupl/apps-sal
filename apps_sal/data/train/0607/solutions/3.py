import math


def solve(arr, n):
    g = 0
    count = 0
    for i in arr:
        g = math.gcd(max(i, g), min(i, g))
        if g == 1:
            g = 0
            count += 1
    if g > 1 and count == 0:
        print(-1)
        return
    print(count)


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(arr, n)


main()
