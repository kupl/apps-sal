def find_highest_power_2(num):
    n=0
    while 2**n <= num:
        n += 1
    return n-1    

def add_binary(a,b):
    sum = a + b
    number = 0
    while sum != 0:
        place_holder = find_highest_power_2(sum)
        number += 10**place_holder
        sum = sum - 2**place_holder
    return str(number)     
        

