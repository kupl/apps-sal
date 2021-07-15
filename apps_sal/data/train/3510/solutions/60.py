def count_red_beads(n):
  count = 0
  if n < 2:
    return 0
  for x in range(1,n):
    count += 2
  return count
