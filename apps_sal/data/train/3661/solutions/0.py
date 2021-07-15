def find_part_max_prod(n):
  if n == 1: return [[1], 1]
  q, r = divmod(n, 3)
  if r == 0: return [[3]*q, 3**q]
  if r == 1: return [[4] + [3]*(q - 1), [3]*(q - 1) + [2, 2], 3**(q - 1) * 2**2]
  return [[3]*q + [2], 3**q * 2]
