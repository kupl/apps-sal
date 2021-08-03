def solve(arr):
    cnt = 0
    arr.sort()
    while(arr[2] < (arr[0] + arr[1])):
        arr[0] -= 1
        arr[1] -= 1
        cnt += 1
    return cnt + arr[0] + arr[1]
