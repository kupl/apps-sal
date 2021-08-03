def alternateCase(s):
    # return s.swapcase() python's swapcase
    def my_own_swapcase(w): return ''.join([l.lower() if l.isupper() else l.upper() if l.islower() else l for l in w])
    return my_own_swapcase(s)
