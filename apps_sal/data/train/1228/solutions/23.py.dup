# cook your dish here
for tc in range(int(input())):
    N1 = int(input())
    P1 = set()
    Q1 = set()
    for i in range(4 * N1 - 1):
        firt, sec1 = map(int, input().split())
        if firt in P1:
            P1.remove(firt)
        else:
            P1.add(firt)
        if sec1 in Q1:
            Q1.remove(sec1)
        else:
            Q1.add(sec1)
    print(*P1, *Q1)
