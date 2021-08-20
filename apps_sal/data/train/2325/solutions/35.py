import sys
'・‥…━━━☆・‥…━━━☆・‥…━━━☆'
read = sys.stdin.read
readline = sys.stdin.readline
'・‥…━━━☆・‥…━━━☆・‥…━━━☆'


def main():
    S = readline().rstrip()
    T = readline().rstrip()
    Q = int(readline())
    l = len(S)
    m = len(T)
    S_acc = [0] * (l + 1)
    T_acc = [0] * (m + 1)
    for i in range(l):
        ch = 1 if S[i] == 'A' else 2
        S_acc[i + 1] = S_acc[i] + ch
    for i in range(m):
        ch = 1 if T[i] == 'A' else 2
        T_acc[i + 1] = T_acc[i] + ch
    for i in range(Q):
        (a, b, c, d) = list(map(int, readline().split()))
        first = S_acc[b] - S_acc[a - 1]
        second = T_acc[d] - T_acc[c - 1]
        if (first - second) % 3 == 0:
            print('YES')
        else:
            print('NO')


def __starting_point():
    INF = float('INF')
    MOD = 10 ** 9 + 7
    sys.setrecursionlimit(10 ** 5)
    '・‥…━━━☆・‥…━━━☆・‥…━━━☆'
    main()


__starting_point()
