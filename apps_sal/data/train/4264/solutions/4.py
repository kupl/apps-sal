def is_power(n):
    if n != int(n):
        return False
    if n == 1:
        return True
    elif n > 1:
        return is_power(n/2)
    else:
        return False

def operation(a,b):
    num_operation = 0
    while a > b or is_power(a) is not True:
        if a % 2 != 0:
            a = (a-1) / 2
            num_operation += 1
        else:
            a = a/ 2
            num_operation += 1
    while a < b:
        a = a * 2
        num_operation += 1
    return num_operation
