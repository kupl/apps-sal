line1 = [int(x) for x in input().split()]
n = line1[0]
k = line1[1]
arr = []
while(n > 0):
    arr.append(int(input()))
    n -= 1
arr.sort()
i = 0
j = k - 1
mini = 110
if j >= len(arr):
    print(arr[len(arr) - 1] - arr[0])

else:
    while(j < len(arr)):
        mini = min(arr[j] - arr[i], mini)
        i += 1
        j += 1

    print(mini)
