from collections import defaultdict


def getlist():
    return list(map(int, input().split()))


def main():
    s = list(input())
    N = len(s)
    judge = "Yes"
    if s[0] == "0":
        judge = "No"
    if s[N - 1] == "1":
        judge = "No"
    for i in range(N - 2):
        if s[i] != s[N - 2 - i]:
            judge = "No"
    if judge == "No":
        print(-1)
        return

    c = 1
    d = N
    for i in range(N - 1):
        if s[i] == "1":
            print(c, c + 1)
            c += 1
        else:
            print(c, d)
            d -= 1


def __starting_point():
    main()


__starting_point()
