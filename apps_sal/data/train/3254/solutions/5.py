def any_odd(x):
    # Write code here...
    a = bin(x)[2:]
    b = a[-2::-2]
    return 1 if '1' in b else 0
