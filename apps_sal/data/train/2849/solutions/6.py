def peak(arr):
  return next(iter(i for i in range(len(arr)) if sum(arr[:i]) == sum(arr[i+1:])), -1)
