def evil(n):
    bin_str = str(bin(n))
    sum = bin_str[2:].count('1')
    msg = "It's Evil!"
    if sum % 2:
        msg = "It's Odious!"
    return msg
