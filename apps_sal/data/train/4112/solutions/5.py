def penultimate(a):
    """Return the penultimate element from a given list.
    
    args:
        a: the input list
    """
    if len(a) < 2:
        raise ValueError('List must contain at least two elements')
    else:
        return a[-2]
