def bin2gray(bits):
  bits.reverse()
  return list(reversed([x if i >= len(bits) - 1 or bits[i + 1] == 0 else 1 - x for i, x in enumerate(bits)]))
  
def gray2bin(bits):
  for i, x in enumerate(bits):
    if i > 0 and bits[i - 1] != 0: bits[i] = 1 - x
  return bits
