import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    S = input()
    T = input()
    Scnt = [0] * (len(S) + 1)
    for i in range(len(S)):
        if S[i] == 'A':
            Scnt[i + 1] = Scnt[i] + 1
        else:
            Scnt[i + 1] = Scnt[i] + 2
    
    Tcnt = [0] * (len(T) + 1)
    for i in range(len(T)):
        if T[i] == 'A':
            Tcnt[i + 1] = Tcnt[i] + 1
        else:
            Tcnt[i + 1] = Tcnt[i] + 2
    
    Q = int(input())
    for _ in range(Q):
        a,b,c,d = map(int,input().split())
        a -= 1
        c -= 1
        if (Scnt[b] - Scnt[a] - Tcnt[d] + Tcnt[c])%3 == 0:
            print('YES')
        else:
            print('NO')
def __starting_point():
    main()
__starting_point()
