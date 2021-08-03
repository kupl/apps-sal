import sys


def main():
    s = sys.stdin.readline
    n, k = list(map(int, s().split()))
    save = {}
    for i in range(1, n + 1):
        save[i] = 0
    for i in range(k):
        try:
            c, v = s().split()
            v = int(v)
            if save[v] == 1:
                save[v] = 0
            elif save[v] == 0:
                save[v] = 1
            ans = 0
            for i in range(1, n + 1):
                if save[i] == 1:
                    ans += 1
            print(ans)
        except:
            for i in range(1, n + 1):
                save[i] = 0
            print(0)


def __starting_point():
    main()


__starting_point()
