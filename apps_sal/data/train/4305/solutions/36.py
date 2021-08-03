def order_weight(strng):
    return ' '.join(sorted(sorted(strng.split()), key=lambda num_str: sum(int(digit) for digit in num_str)))
