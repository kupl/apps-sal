def binary_array_to_number(arr):
  return sum(value*(2**index) for index, value in enumerate(arr[::-1]))
