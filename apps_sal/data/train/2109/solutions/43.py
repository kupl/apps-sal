def main():
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        ref = a * b
        s = int(ref ** 0.5)
        ans = 2 * s - 1
        if s * (s + 1) >= ref:
            ans -= 1
        if s * s == ref and a != b:
            ans -= 1
        print(ans)
def __starting_point():
    main()
__starting_point()
