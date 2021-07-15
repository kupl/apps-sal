def divide(weight):
    weight = weight / 2
    if weight % 2 == 0:
        return True
    elif (weight + 1) % 2 ==0 and weight > 1:
        return True
    else: 
        return False

