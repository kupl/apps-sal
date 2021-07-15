def cyclic_string(s):
    for i in range(1, len(s)):
        # Check to see if s is in the first i characters repeated enough to be of len(s) 
        if s in s[:i] * (len(s) // i) * 2:
            return i
    # Must use whole string
    return len(s)
