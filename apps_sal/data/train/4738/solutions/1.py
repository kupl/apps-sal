def find(rats):
    """
    The rule the king should use is the following:
        1) Label all bottle from 1 to 1000
        2) Label all rats from 0 to 9
        3) For each rat r, make it drink the bottle b if the binary representation of b has it's rth bit
           is one.
    Reconstruct the label of the poisonned bottle by computing the base-10 representation:
    """
    return sum(map(lambda x: pow(2,x), rats))
