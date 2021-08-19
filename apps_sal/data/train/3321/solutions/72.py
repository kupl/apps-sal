def dec_to_bin(n):
    bin_list = []
    x = n
    while x > 0:
        bit = x % 2
        bin_list.append(bit)
        x //= 2
    return bin_list


def evil(n):
    binary = dec_to_bin(n)
    if binary.count(1) % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"
