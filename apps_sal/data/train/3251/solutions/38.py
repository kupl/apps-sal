import math
def primeFactors(number):

    # create an empty list and later I will
    # run a for loop with range() function using the append() method to add elements to the list.
    prime_factors = []

    # First get the number of two's that divide number
    # i.e the number of 2's that are in the factors
    while number % 2 == 0:
        prime_factors.append(2)
        number = number / 2

    # After the above while loop, when number has been
    # divided by all the 2's - so the number must be odd at this point
    # Otherwise it would be perfectly divisible by 2 another time
    # so now that its odd I can skip 2 ( i = i + 2) for each increment
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            prime_factors.append(int(i))
            number = number / i

    if number > 2:
        prime_factors.append(int(number))
        
    distinct_set = sorted(set(prime_factors))
    
    output = ""
    
    for i in distinct_set:
        
        if(prime_factors.count(i) == 1):
            
            output = output + '(' + str(i) + ')'
        else:
            output = output + '(' + str(i)+ '**' + str(prime_factors.count(i)) +  ')'
        
    return output
