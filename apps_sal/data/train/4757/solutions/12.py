import sys
def input():
    return sys.stdin.readline()[:-1]
def main():
    for _ in range(int(input())):
        n, m, a, b = list(map(int,input().split()))
        if abs(n/b - m/a) > 0.00001:
            print("NO")
        else:
            print("YES")
            ans = [["0"]*m for k in range(n)]
            for k in range(n):
                for l in range(k*a,k*a+a):
                    ans[k][l%m] = "1"
            for e in ans:
                print("".join(e))
def __starting_point():
    main()

__starting_point()
