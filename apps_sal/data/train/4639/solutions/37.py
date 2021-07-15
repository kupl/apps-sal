def power_of_two(x):
    power = 0
    
    while True:
        some_value = pow(2, power)
        if some_value == x:
            return True
            break
        elif some_value > x:
            return False
            break
        
        power += 1
