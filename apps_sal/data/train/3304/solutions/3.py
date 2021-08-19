def is_inertial(arr):
    """Try to maximize performance by only looping once over array"""
    maxnr_odd = minnr_odd = maxnr_even = maxnr2nd_even = None
    for nr in arr:
        if nr % 2 == 0:
            if maxnr_even is None:
                maxnr_even = nr
            elif nr > maxnr_even:
                (maxnr_even, maxnr2nd_even) = (nr, maxnr_even)
            elif maxnr2nd_even is None or maxnr2nd_even < nr:
                maxnr2nd_even = nr
        else:
            if minnr_odd is None or minnr_odd > nr:
                minnr_odd = nr
            if maxnr_odd is None or maxnr_odd < nr:
                maxnr_odd = nr
    return maxnr_even is not None and maxnr_odd is not None and (minnr_odd is not None) and (maxnr_odd < maxnr_even) and (maxnr2nd_even is None or minnr_odd > maxnr2nd_even)
