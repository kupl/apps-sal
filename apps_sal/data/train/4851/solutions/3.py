def sort_ranks(ranks):
  return sorted(ranks, key=lambda s: tuple(int(x) for x in s.split('.')))
