def tidyNumber(n):
    """
    given a number
    return True if each number following is >=
    """
    if n != int(''.join(sorted(str(n)))):
        return False
    return True
