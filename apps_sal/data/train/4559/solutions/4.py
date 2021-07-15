def ones_complement(binary_number):
  return ''.join('0' if int(n) else '1' for n in binary_number)
