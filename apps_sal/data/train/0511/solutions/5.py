import sys
input = sys.stdin.readline


def main():
    N = int(input())
    a = list(map(int, input().split()))

    s = 0
    for i in a:
        s ^= i

    for i in a:
        ans = s ^ i
        print(ans, sep=' ', end=' ')


main()
