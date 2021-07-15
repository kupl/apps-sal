def evil(n):
    count_one = str(bin(n)).count('1')
    if count_one % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"
