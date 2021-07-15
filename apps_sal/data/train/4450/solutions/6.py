def consecutive(arr):
  l = len(arr)
  return max(arr) - min(arr) + 1 - l if l>1 else 0
