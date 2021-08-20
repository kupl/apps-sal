from math import ceil
from itertools import accumulate
digs = map(int, '031415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
MEMO = tuple((ceil(s ** 0.5) for s in accumulate((d * d for d in digs))))
square_pi = MEMO.__getitem__
