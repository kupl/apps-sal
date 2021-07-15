from operator import *

def sequence_classifier(arr):
  for op, code in {eq: 5, gt: 1, lt: 3, ge: 2, le: 4}.items():
    if all(op(d, 0) for d in map(sub, arr[1:], arr)):
      return code
  return 0
