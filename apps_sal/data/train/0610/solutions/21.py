for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().strip().split()))
    Positions = []
    not_followed = 0
    for i in range(N):
        if A[i] == 1:
            Positions.append(i + 1)
    for i in range(len(Positions) - 1):
        if Positions[i + 1] - Positions[i] < 6:
            not_followed += 1
    if not_followed == 0:
        print('YES')
    else:
        print('NO')
