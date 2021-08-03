def power_of_two(x):
    # your code here
    if x == 0:
        return False  # checking the 1st case
    while (x != 1):
        if (x % 2 != 0):
            return False
        x = x // 2  # //floor division it will give round numbersfor ex:1.5 means it will give 1
    return True
