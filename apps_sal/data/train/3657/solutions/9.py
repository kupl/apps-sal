def series_slices(digits, n):
  return [list(map(int, digits[i:i+n])) for i in range(len(digits)-n+1)] if n <= len(digits) else int("")
