def find_longest(arr):
    max = -1
    result = 0
    for num in arr:
      l = len(list(str(num)))
      if l > max:
        max = l
        result = num
    return result

