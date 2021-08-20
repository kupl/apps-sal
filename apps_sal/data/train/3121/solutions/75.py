def solve(arr):
    abs_arr = [abs(n) for n in arr]
    for n in set(abs_arr):
        if not (n in arr and -n in arr):
            return arr[abs_arr.index(n)]
