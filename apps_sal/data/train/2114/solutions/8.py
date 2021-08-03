N, E = 0, 0
Cost, Edges = [], []
Answer = 0.0


def Solve():
    nonlocal Answer
    for e in Edges:
        Answer = max(Answer, (1.0 * (Cost[e[0]] + Cost[e[1]]) / (1.0 * e[2])))


def ReadInput():
    nonlocal N, E, Cost, Edges
    N, E = list(map(int, input().split()))
    Cost = list(map(int, input().split()))
    for i in range(0, E):
        x, y, c = list(map(int, input().split()))
        Edges.append((x - 1, y - 1, c))


def PrintOutput():
    print(Answer)


def main():
    ReadInput()
    Solve()
    PrintOutput()


main()
