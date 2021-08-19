test = int(input())
for _ in range(test):
    n = int(input())
    array = list(map(int, input().split()))
    maxi = max(array)
    index = []
    for i in range(n):
        if array[i] == maxi:
            index.append(i)
    if len(index) == 1:
        print(n // 2)
    elif index[len(index) - 1] - index[0] >= n // 2:
        print(0)
    else:
        print(n // 2 - (index[len(index) - 1] - index[0]))
