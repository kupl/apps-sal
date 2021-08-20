t = int(input())
for i in range(t):
    (n, k, e, m) = tuple(map(int, input().split()))
    scores = []
    for j in range(n - 1):
        scores.append(sum(list(map(int, input().split()))))
    scores.sort(reverse=True)
    bsc = scores[k - 1]
    msc = sum(list(map(int, input().split())))
    mini = bsc - msc + 1
    if mini < 0:
        print(0)
    elif mini > m:
        print('Impossible')
    else:
        print(mini)
