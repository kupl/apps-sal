from sys import stdin, stdout


def main():
    for _ in range(int(input())):
        (r, c) = map(int, input().split())
        (x, y) = map(int, input().split())
        res1 = max(r - 1 - x, x)
        res2 = max(c - 1 - y, y)
        print(res1 + res2)


main()
