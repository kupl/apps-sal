def sum_digits(number):
    #initializing sum to zero
    sum=0
    #for each digit(e) in number
    for e in str(abs(number)):
        #adding each digit to sum
        sum+=int(e)
    #returning sum
    return sum
