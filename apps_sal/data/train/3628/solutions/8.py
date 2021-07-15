from numpy import roll

def rotate(arr, n):
  return list(roll(arr, n))
