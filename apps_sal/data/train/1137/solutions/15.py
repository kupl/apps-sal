t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()
    idx = n - 1
    flag = 0
    for i in range(n):
        if i == idx:
            break
        while idx > i + 1 and array[i] + array[idx] > 2000:
            idx -= 1
        if array[i] + array[idx] == 2000:
            flag = 1
            break
    if flag == 1:
        print('Accepted')
    else:
        print('Rejected')
