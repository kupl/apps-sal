def sharkovsky(a, b):
    if a == b:
        return False
    if a <3:
        return False
    if b<3:
        return True
    print(a,b)
    higher = max(a,b)
    lower = min(a,b)
    number = 3
    while number <= higher:
        if number == a:
            return True
        if number == b:
            return False
        number = number + 2
    counter = 3
    number = 2 * counter
    while number <= higher:
        if number == a:
            return True
        if number == b:
            return False
        counter = counter + 2
        number = 2 * counter
    counter = 3
    exponential = 1
    number = (2**exponential) * counter
    while number <= higher:
        if number == a:
            return True
        if number == b:
            return False
        counter = counter + 2
        exponential = exponential + 1
        number = (2**exponential) * counter
    counter = 3
    exponential = 2
    number = (2**exponential) * counter
    while number <= higher:
        if number == a:
            return True
        if number == b:
            return False
        counter = counter + 2
        exponential = exponential + 1
        number = (2**exponential) * counter
    exponential = 1
    number = (2**exponential) 
    while number >= lower:
        if number == a:
            return True
        if number == b:
            return False
        exponential = exponential - 1
        number = (2**exponential) 
    number = higher 
    while number >= lower:
        if number == a:
            return True
        if number == b:
            return False
        number = (number - 2)
    return False
