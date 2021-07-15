from operator import itemgetter

def sort_dict(d):
  'return a sorted list of tuples from the dictionary'
  return sorted(d.items(), key=itemgetter(1), reverse=True)
