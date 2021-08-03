import sys
input = sys.stdin.readline


def solve(a, b):
    score = a * b
    l, r = 0, int(1e18)
    while r - l > 1:
        k = (l + r) // 2
        if k**2 < score:
            l = k
        else:
            r = k

    ans1 = l * 2 - 1
    if a <= l:
        ans1 -= 1
    if b <= l and a != b:
        ans1 -= 1

    ans2 = 0
    if l * r < a * b:
        ans2 = l * 2
        if a <= l:
            ans2 -= 1
        if b <= l and a + b != l + r:
            ans2 -= 1

    ans = max(ans1, ans2)
    return ans


def main():
    q = int(input())
    for i in range(q):
        a, b = list(map(int, input().split()))
        ans = solve(a, b)
        print(ans)


def __starting_point():
    main()


__starting_point()
