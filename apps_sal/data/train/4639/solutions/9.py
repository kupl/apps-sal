def power_of_two(x):
    return True if sum((int(i) for i in bin(x) if i.isdigit())) == 1 else False
