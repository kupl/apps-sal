def shared_bits(a, b):
    return True if format(a & b, 'b').count('1') > 1 else False
