def loose_change(coins, change):
  return search(sorted(coins, reverse=True), change)

def search(coins, x, n=0):
  if x == 0: return n
  m = 9999
  for c in coins:
    if x >= c:
      q, r = divmod(x, c)
      m = min(m, search(coins, r, n + q))
  return m
