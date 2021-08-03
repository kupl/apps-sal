def reverse_number(n):
    rev = 0
    temp = n
    dig = 0
    if(n < 0):
        n = abs(n)
    while(n > 0):
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if(temp < 0):
        return -rev
    else:
        return rev
