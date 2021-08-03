def int_to_bin(n):

    bin_lst = []
    x = n
    while x > 0:
        bit = x % 2
        bin_lst.append(bit)
        x //= 2

    return bin_lst[::-1]


def evil(n):
    if int_to_bin(n).count(1) % 2 == 1:
        return "It's Odious!"
    else:
        return "It's Evil!"
