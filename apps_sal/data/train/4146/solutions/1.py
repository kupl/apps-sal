def is_sorted_and_how(arr):
  if arr == sorted(arr):
      return 'yes, ascending'
  elif arr == sorted(arr, reverse=True):
      return 'yes, descending'
  return 'no'
