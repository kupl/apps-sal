def is_divisible_by_6(s):
  return [str(n) for n in [int(s.replace('*', str(i))) for i in range(10)] if n % 6 == 0]
