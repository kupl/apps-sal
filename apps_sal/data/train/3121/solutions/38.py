def solve(arr):
    end = 0
    x = 0
    while end == 0:
        k = 1
        i = arr[x]
        for j in arr:
            if i == j * -1:
                k = 0
        if k == 1:
            ans = i
            end = 1
        x = x + 1
    return ans
