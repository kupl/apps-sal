get_weight=lambda s:sum(ord(e)for e in s.swapcase()if e.isalpha())
