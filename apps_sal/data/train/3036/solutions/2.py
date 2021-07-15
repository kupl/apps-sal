def abacaba(k):
    return chr((k & -k).bit_length() + 96)
