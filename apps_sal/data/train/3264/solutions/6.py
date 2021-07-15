from math import ceil, log, pi, e
count = lambda n: int(ceil(log(2*pi*n, 10)/2+n*log(n/e, 10)))
