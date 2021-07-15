def hamming_weight(x):
  count = 0
  while x:
    x &= x-1
    count += 1
  return count

