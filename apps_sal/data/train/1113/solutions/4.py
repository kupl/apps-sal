
def solve():
    N = int(input())
    V = [0] * 10001
    I = list(map(int, input().split()))
    for i in I:
        V[i] += 1
    Ans = 0
    for i in range(len(V)):
        if V[i] > V[Ans]:
            Ans = i
    print(Ans, V[Ans])


def main():
    t = int(input())
    for i in range(t):
        solve()


main()
