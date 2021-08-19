n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

ans = []
ans.append(1)

for i in range(1, n):
    val = arr[i]
    for j in range(i - 1, -2, -1):
        if(j == -1):
            arr[j + 1] = val
            ans.append(1)
            break

        if(arr[j] < val):
            arr[j + 1] = arr[j]
        else:
            arr[j + 1] = val
            ans.append(j + 2)
            break

    #print(arr, val)

print(*(ans), sep='\n')
