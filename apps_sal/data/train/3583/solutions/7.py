def binary_array_to_number(arr):
    if type(arr) is list and len(arr)>0:
      return int(''.join(str(e) for e in arr), 2)
    return -1
