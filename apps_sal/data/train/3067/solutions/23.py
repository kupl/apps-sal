# Note: Cuboid was misspelled and camelCased in problem statement, tests, and
# required function signature.

import functools
import operator

def getVolumeOfCubiod(*dimensions):
    """Compute volume to an arbitrary dimension :)."""
    return functools.reduce(operator.mul, dimensions, 1)
