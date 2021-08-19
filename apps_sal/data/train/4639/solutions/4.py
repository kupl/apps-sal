def power_of_two(x):
    # your code here
    return (x & (x - 1) == 0) and (x > 0)
