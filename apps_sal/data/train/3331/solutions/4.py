def solve(arr, n):
    caught = 0
    for i in range(0, len(arr)):
        if arr[i] == 'C':
            for j in range(0, len(arr)):
                if abs(i - j) <= n and arr[j] == 'D' and arr[i] != 'X':
                    arr[i], arr[j] = 'X', 'X'
                    caught += 1
    return caught
