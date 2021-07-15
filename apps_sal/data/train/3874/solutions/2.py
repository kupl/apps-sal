def sort_twisted37(arr):
  twisted = lambda n: int(''.join('3' if c=='7' else '7' if c == '3' else c for c in str(n)))
  return sorted(arr, key=twisted)
