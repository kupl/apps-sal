def abacaba(k):
    return chr(96 + (k & -k).bit_length())
