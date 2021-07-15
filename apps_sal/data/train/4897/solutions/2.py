def binary_gcd(x, y):

  if x==0 and y==0:
    return 0

  def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)

  return sum( c == '1' for c in bin(gcd(x, y))[2:] )
