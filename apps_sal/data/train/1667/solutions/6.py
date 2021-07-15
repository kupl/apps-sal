def unflatten(flat_array, depth, direction=1):
    if depth == 0: return flat_array
    if direction == 1:
      result, j = [], 0
      length = len(flat_array)
      while j < length:
        if isinstance(flat_array[j], list):
          result.append(unflatten(flat_array[j], 1, direction=1))
          j += 1
        else:
          remainder = flat_array[j] % (length - j)
          if remainder < 3:
              result.append(flat_array[j])
              j += 1
          else:
              result.append(flat_array[j:j+remainder])
              j += remainder
      return unflatten(result, depth-1, direction=-1)
    else:
      length = len(flat_array)
      result, j = [], length - 1
      while j >= 0:
        if isinstance(flat_array[j], list):
          result.append(unflatten(flat_array[j], 1, direction=-1))
          j -= 1
        else:
          remainder = flat_array[j] % (j + 1)
          if remainder < 3:
              result.append(flat_array[j])
              j -= 1
          else:
              result.append(flat_array[j-remainder+1:j+1])
              j -= remainder
      return unflatten(result[::-1], depth-1, direction=1)
