def round_to_next5(n):
    if not n % 5:
      return n
    else:
      return round_to_next5(n + 1)
