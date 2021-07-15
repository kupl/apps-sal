def triple_double(num1, num2):
    for i in range(10):
        if str(i) * 3 in str(num1):
            if str(i) * 2 in str(num2):
                return 1
            else:
                return 0
    return 0
