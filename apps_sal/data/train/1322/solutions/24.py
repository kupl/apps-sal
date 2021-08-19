for i in range(int(input())):
    (n, k) = map(int, input().split())
    Q = list(map(int, input().split()))
    Q.sort(reverse=True)
    score = Q[k - 1]
    result = 0
    for i in Q:
        if i >= score:
            result = result + 1
    print(result)
