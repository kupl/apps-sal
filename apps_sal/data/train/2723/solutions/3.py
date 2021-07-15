nbrs = 'zero one two three four five six seven eight nine'.split()

def average_string(s):
  try:
    return nbrs[sum(map(nbrs.index, s.split())) // len(s.split())]
  except:
    return 'n/a'
