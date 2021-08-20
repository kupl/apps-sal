from operator import contains
from functools import partial
L = {5, 13, 103, 563, 329891, 36846277}
am_i_wilson = partial(contains, L)
