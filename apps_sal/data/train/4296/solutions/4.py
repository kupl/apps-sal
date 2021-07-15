import heapq

def largest(n,xs):
  """Find the n highest elements in a list"""
  return sorted(heapq.nlargest(n, xs))
