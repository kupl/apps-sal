def sel_number(n, d):
    count = 0
    # Check for any invalid pairs
    def any_invalid(digits):
        # Pair up elements of a sequence 0,1 then 1,2 then 2,3 etc.
        for a, b in zip(digits, digits[1:]):
            # Compare each pair of digits in a sequence
            if a >= b or b - a > d:
                return True
        return False
    
    for i in xrange(10, n + 1):
        if any_invalid([int(c) for c in str(i)]):
            continue
        count += 1
    return count
