from collections import Counter

def majority(arr):
  counter = Counter(arr)
  best = counter.most_common(2)
  if not best:
      return None
  elif len(best) == 1 or best[0][1] != best[1][1]:
      return best[0][0]

