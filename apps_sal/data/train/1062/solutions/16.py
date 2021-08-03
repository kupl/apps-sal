n = int(input())
temp = [n for i in range(2 * n - 1)]
arr = []
firstelement = temp[:]
arr.append(firstelement)
for i in range(1, n):
    temp[i:-i] = [n - i for j in range(len(temp[i:-i]))]
    ttemp = temp[:]
    arr.append(ttemp)
for i in range(len(arr) - 2, 0, -1):
    appendtemp = arr[i][:]
    arr.append(appendtemp)
arr.append(arr[0])
for i in arr:
    for j in i:
        print(j, end=" ")
    print("\n")
