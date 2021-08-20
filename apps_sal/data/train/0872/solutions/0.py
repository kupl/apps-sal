for t in range(int(input())):
    (n, a, b, k) = map(int, input().split())
    solvedbychef = 0
    solvedbyappy = 0
    for i in range(n + 1):
        if i % a == 0 and i % b == 0:
            continue
        elif i % a == 0:
            solvedbyappy += 1
        elif i % b == 0:
            solvedbychef += 1
    totalsolved = solvedbychef + solvedbyappy
    if totalsolved >= k:
        print('Win')
    else:
        print('Lose')
