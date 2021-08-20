def reverse_number(n):
    """
    Reverse a number, preserve negative sign
    """
    s = str(n)
    ret = int('-{}'.format(s[:0:-1]) if '-' in s else s[::-1])
    return ret
