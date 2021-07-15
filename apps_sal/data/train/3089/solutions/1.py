import re

def dashatize(num):
  return 'None' if num is None else '-'.join(w for w in re.split(r'([13579])', str(abs(num))) if len(w)>0)
