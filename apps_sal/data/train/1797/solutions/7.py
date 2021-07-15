
import itertools

H = sorted([
  2**i * 3**j * 5**k
  for i, j, k in itertools.product(xrange(50), xrange(50), xrange(50))
])
hamming = lambda n, H=H: H[n-1]
