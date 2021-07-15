def solve(arr, cur = [1]):
  return solve(arr[1:], [x*y for x in cur for y in arr[0]]) if arr else max(cur)
