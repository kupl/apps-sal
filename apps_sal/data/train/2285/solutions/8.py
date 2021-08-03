import sys


def main():
    def input():
        return sys.stdin.readline()[:-1]
    t = int(input())
    for z in range(t):
        flag = 0
        n = int(input())
        s = [int(x) for x in input()]
        for limit in range(10):
            ans = [0 for k in range(n)]
            p = 0
            for now in range(limit + 1):
                for k in range(p, n):
                    if s[k] == now:
                        p = k
                        ans[k] = 1
            p = 0
            for now in range(limit, 10):
                for k in range(p, n):
                    if s[k] == now and ans[k] == 0:
                        p = k
                        ans[k] = 2
            if 0 not in ans:
                flag = 1
                print(*ans, sep="")
                break
        if flag == 0:
            print("-")


def __starting_point():
    main()


__starting_point()
