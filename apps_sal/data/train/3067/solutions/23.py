
import functools
import operator


def getVolumeOfCubiod(*dimensions):
    """Compute volume to an arbitrary dimension :)."""
    return functools.reduce(operator.mul, dimensions, 1)
