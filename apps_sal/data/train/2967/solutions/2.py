def bin_to_hex(bin_stg):
    return base_to_base(bin_stg, 2, 16)

def hex_to_bin(hex_stg):
    return base_to_base(hex_stg, 16, 2)

def base_to_base(num_stg, from_base, to_base):
    digits = "0123456789abcdef"
    result, n = "", sum(digits.index(d) * from_base**i for i, d in enumerate(num_stg.lower()[::-1]))
    while n > 0:
        d = n % to_base
        result, n = digits[d] + result, n // to_base
    return result or "0"
