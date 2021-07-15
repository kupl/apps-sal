def convert_bits(a, b):
  A = f'{abs(a):040b}'
  B = f'{abs(b):040b}'
  diffs = 0
  for i, j in zip(A, B):
    if i != j:
      diffs+=1
  return diffs

