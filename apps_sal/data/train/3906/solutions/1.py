def total(arr):
  from math import factorial as fact

  choose = lambda a, b: fact(a) / (fact(a-b) * fact(b))

  return sum(choose(len(arr)-1, i) * v for i, v in enumerate(arr))
