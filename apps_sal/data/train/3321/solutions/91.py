def evil(n):

    one_sum = 0
    while n:
        one_sum += n & 1
        n>>=1

    if one_sum % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"

