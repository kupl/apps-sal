def convert_bits(a, b):
    return format(a ^ b, 'b').count('1')
