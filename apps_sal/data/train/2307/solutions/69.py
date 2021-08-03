import sys
input = sys.stdin.readline

mod = 1000000007


def main():
    n, a, b = list(map(int, input().split()))
    X = list(map(int, input().split()))
    useb = b // a
    ans = 0
    for i in range(n - 1):
        d = X[i + 1] - X[i]
        if d > useb:
            ans += b
        else:
            ans += d * a

    print(ans)


main()
