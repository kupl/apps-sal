def isprime(x): #function to check if number is a prime number
    number = x
    if number==2:
        return(True)
    else:
        for num in range(2,number):
            if number%num ==0:
                return(False)
        else:
            return(True)

def num_primorial(num_of_nums):
    counter = 0 # counter to keep track of how many numbers prime numbers we've multipled
    number = 2 #arbitray number to start keeping track of prime numbers
    primorial=1 #return variable which we will multiple all discovered prime numbers by until counter == num_of_nums

    
    for x in range(2,10000):
        if isprime(number) == True: 
            primorial *=x
            number+=1#keep our number counter going up to test for more prime numbers
            counter+=1
            if counter == num_of_nums:# to break the loop once we have the desired amount of prime numbers multipled
                break
        else:
            number+=1 #keep our number counter going up to test for more prime numbers
    return(primorial)
            

