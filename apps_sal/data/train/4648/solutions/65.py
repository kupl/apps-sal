def automorphic(n):
    """
    given an integer n
    test to see if n's square ends in the same digits as the number itself.
    return boolean
    """
    charLength = len(str((n)))
    squared = str(n ** 2)

    automorphicTest = int(squared[-(charLength):])

    if automorphicTest == n:
        return "Automorphic"
    else:
        return "Not!!"
