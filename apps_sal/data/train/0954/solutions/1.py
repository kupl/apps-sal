t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    sum1 = 0
    sum2 = 0
    for i in range(n):
        arr.append(i + 1)
    arr2 = arr[0:n - 1]
    for i in range(n):
        sum1 = sum1 + (arr[i] * arr[i] * arr[i])
    for i in range(len(arr2)):
        sum2 = sum2 + (arr2[i] * arr[i] * arr[i])
    if n == 1:
        print("1")
    else:
        print(sum1 + sum2)
