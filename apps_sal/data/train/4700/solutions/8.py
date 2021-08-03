def solve(arr, cur=[]):
    return (solve(arr[1:], [x * y for x in cur for y in arr[0]]) if cur else solve(arr[1:], arr[0])) if arr else max(cur)
