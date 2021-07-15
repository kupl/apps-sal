def largest_sum(s):
  ar = s.split("0")
  max = 0
  for e in ar:
    a = [int(d) for d in e]
    if max < sum(a):
      max = sum(a)
  return max
