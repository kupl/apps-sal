def climb(n):
    return list(climb_iterator(n))
    
def climb_iterator(n):
    cursor = 0
    for digit in bin(n)[2:]:
        cursor = 2 * cursor + int(digit)
        yield cursor
