def can_jump(arr):
    length = len(arr)
    i = length - 2
    while i >= 0:
      if arr[i] + i >= length:
        length = i
      i-=1
    return length == 0
