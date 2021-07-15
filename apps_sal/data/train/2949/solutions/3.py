from itertools import zip_longest

def split_and_add(xs, n):
  return split_and_add([(a or 0) + b for a, b in zip_longest(xs[:len(xs)//2][::-1], xs[len(xs)//2:][::-1])][::-1], n-1) if n else xs
