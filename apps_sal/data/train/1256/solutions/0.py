t = int(input())
res = []
for i in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    num_2 = 0
    num = 0
    for j in range(len(arr)):
        if arr[j] == 2:
            num_2 += 1
        if arr[j] > 2:
            num += 1
    res.append(num_2 * num + num * (num - 1) // 2)
for z in res:
    print(z)
