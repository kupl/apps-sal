h = '0123456789abcdef'

def bin_to_hex(binary_string):
    n = 0
    for x in binary_string:
        n = n * 2 + (x == '1')
    result = []
    while n:
        n, r = divmod(n, 16)
        result.append(h[r])
    return ''.join(result[::-1]) or '0'

def hex_to_bin(hex_string):
    n = 0
    for x in hex_string.lower():
        n = n * 16 + h.find(x)
    result = []
    while n:
        n, r = divmod(n, 2)
        result.append(h[r])
    return ''.join(result[::-1]) or '0'
