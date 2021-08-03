def get_weight(s): return sum(ord(e)for e in s.swapcase()if e.isalpha())
