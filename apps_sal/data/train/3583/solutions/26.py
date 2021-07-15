def binary_array_to_number(arr):
  a = len(arr)
  n = 0
  for i in range(len(arr)):
      a-=1
      if arr[i] == 1:
          n += 2**a
  return n
      

