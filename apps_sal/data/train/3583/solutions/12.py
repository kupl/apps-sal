def binary_array_to_number(arr):
  # your code
  binary = "".join([str(n) for n in arr])
  return int(binary, 2)
