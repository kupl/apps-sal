def add_binary(a,b):
    #your code here
    summ = a + b
    binary = ''
    while(True):
        rem = summ % 2
        binary += str(rem)
        summ -= summ % 2
        summ //= 2
        if summ == 0:
            break
    return binary[::-1]
