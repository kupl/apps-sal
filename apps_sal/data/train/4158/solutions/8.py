def letter_check(arr): 
  arr = list([x.lower() for x in arr])
  for i in set(list(arr[1])):
    if i not in arr[0]:
      return False
  return True

