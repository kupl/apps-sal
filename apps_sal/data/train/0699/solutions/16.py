for a in range(int(input())):
    (n, k, d) = map(int, input().split())
    q = map(int, input().split())
    problem = sum(q)
    days = problem // k
    if problem < k:
        print(0)
    elif days <= d:
        print(days)
    else:
        print(d)
