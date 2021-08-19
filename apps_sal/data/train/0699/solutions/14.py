for t in range(int(input())):
    (n, k, d) = list(map(int, input().split()))
    problems = list(map(int, input().split()))
    sum = day = 0
    for i in problems:
        sum += i
    contest = sum // k
    if contest == 0:
        print(0)
    elif contest > d:
        print(d)
    else:
        print(contest)
