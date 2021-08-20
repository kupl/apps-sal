for t in range(int(input())):
    (n, k, e, m) = map(int, input().split())
    stud = n - k - 1
    sum_list = []
    for i in range(n - 1):
        l = list(map(int, input().split()))
        sum_list.append(sum(l))
    score = list(map(int, input().split()))
    sum_sergey = sum(score)
    sum_list.sort()
    x = max(sum_list[stud] + 1 - sum_sergey, 0)
    if x < m:
        print(x)
    else:
        print('Impossible')
