test = int(input())
for _ in range(test):
    (n, m) = map(int, input().split())
    indexArray = list(map(int, input().split()))
    mini = min(indexArray)
    maxi = max(indexArray)
    result = [0 for i in range(n)]
    for i in range(n):
        result[i] = max(maxi - i, i - mini)
        print(result[i], end=' ')
    print()
