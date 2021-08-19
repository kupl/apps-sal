def add_binary(a, b):
    """Adds a and b together and returns a binary string"""
    if a + b >= 0:
        return bin(a + b)[2:]
    else:
        return '-' + bin(a + b)[3:]
