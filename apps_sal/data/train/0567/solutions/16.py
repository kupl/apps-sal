t = int(input())
for _ in range(t):
    n = int(input())
    s = input().split(' ')
    arr = [int(i) for i in s]
    flag = 0
    for i in range(len(arr) - 2):
        if arr[i] == arr[i + 1] and arr[i + 1] == arr[i + 2]:
            flag = 1
            break
    if flag == 0:
        print('No')
    else:
        print('Yes')
