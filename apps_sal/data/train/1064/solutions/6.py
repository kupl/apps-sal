# cook your dish here
def check(arr):
    dic = {0: 'C', 1: 'H', 2: 'E', 3: 'F'}
    for i in range(4):
        if arr[i] != '?':
            if arr[i] != dic[i]:
                return -1
    for i in range(4):
        if arr[i] == '?':
            arr[i] = dic[i]
    return arr


t = int(input())
for _ in range(t):
    arr = input()
    arr = list(arr)
    i = len(arr)

    if i < 4:
        for k in range(i):
            if arr[k] == '?':
                arr[k] = 'A'

    while i > 3:
        if '?' in arr[i - 4:i]:
            if check(arr[i - 4:i]) == -1:
                i -= 1
                continue
            else:
                arr[i - 4:i] = check(arr[i - 4:i])
                i -= 3
        i -= 1
    for k in range(len(arr)):
        if arr[k] == '?':
            arr[k] = 'A'

    res = ''
    for ele in arr:
        res += ele
    print(res)
