def binary_array_to_number(arr):
  binarr = ""
  for i in arr:
        binarr = binarr + str(i)
  return int(binarr, 2)
