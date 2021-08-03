def evil(n):
    bin_number = bin(n)
    count = 0
    for i in bin_number:
        if i == '1':
            count += 1
    if count % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"
