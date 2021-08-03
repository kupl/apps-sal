n = int(input())
arr = list(map(int, input().split()))
arr.sort()
i = 0
count = 0
while(i < n):
    if(i == n - 1):
        i += 1
        count += 1
        continue
    if(arr[i] == arr[i + 1]):
        i += 2
    else:
        i += 1

    count += 1
print(count)
