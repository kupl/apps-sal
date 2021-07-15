def evil(n):
    count_1 = bin(n).count('1')
    msg = "It's Evil!"
    if count_1 % 2:
        msg = "It's Odious!"
    return msg
