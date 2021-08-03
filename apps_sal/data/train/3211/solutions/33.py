def divide(weight):
    for i in range(1, weight):
        if(weight % i == 0):
            if(i % 2 == 0):
                return True
    return False
