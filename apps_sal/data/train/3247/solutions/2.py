def sort_by_height(a):
  people = iter(sorted([i for i in a if i != -1]))
  return [i if i == -1 else next(people) for i in a]
