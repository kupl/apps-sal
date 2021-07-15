def power_of_two(x):
    
    i = 0
    while True:
        num = 2**i
        if num == x:
            return True
        elif num > x:
            return False
        i += 1
