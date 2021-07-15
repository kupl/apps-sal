from math import ceil, log2

def fold_to(distance):
    if distance < 0:
      return None
    if not distance:
      return 0
    return max(0, ceil(log2(distance / 0.0001)))
