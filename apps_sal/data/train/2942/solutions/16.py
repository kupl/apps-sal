from math import log, ceil; fold_to=lambda d: None if d<0 else 0 if d<0.0001 else ceil(log(d*10000,2))
