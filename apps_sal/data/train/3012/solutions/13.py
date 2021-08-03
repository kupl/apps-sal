def shared_bits(a, b):
    bin_a = bin(a)[2:]
    bin_b = bin(b)[2:]

    if len(bin_a) > len(bin_b):
        bin_b = ('0' * (len(bin_a) - len(bin_b))) + bin_b
    if len(bin_a) < len(bin_b):
        bin_a = ('0' * (len(bin_b) - len(bin_a))) + bin_a

    index = 0
    counter = 0
    while index < len(bin_a):
        if bin_a[index] == '1' and bin_b[index] == '1':
            counter += 1

        if counter >= 2:
            return True

        index += 1

    return False
