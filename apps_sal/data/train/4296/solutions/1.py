def largest(n,xs):
  import heapq
  return heapq.nlargest(n,xs)[::-1]
