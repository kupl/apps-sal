def binary_to_string(b): return ''.join(__import__('binascii').unhexlify('%x' % int('0b' + b[i:i + 8], base=2)).decode("utf-8") for i in range(0, len(b), 8))
