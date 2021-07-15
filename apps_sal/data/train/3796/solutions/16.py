from itertools import starmap, zip_longest
or_arrays = lambda a1, a2, f=0: list(starmap(int.__or__, zip_longest(a1, a2, fillvalue=f)))
