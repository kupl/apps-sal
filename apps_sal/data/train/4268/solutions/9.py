def next_num(n):

    '''
    I work on input number converting it to string throughout the code.
    We check if number is polydivisible, if not we find where in the number 
    first problem occurs and then substitute proper part into the initial 
    number and check over again.
    '''
    number=str(n+1)

                                                    # Inner funtion checking for polydivisibility.
                                                    # It returns place where polydivisibility test fails at first or 
                                                    # 0 if number is polydivisible
    def isNumPoly(number):
        for i in range(1,len(number)+1):
            if not (int(number[0:i]))%(i)==0:
                return i
        return 0
                                                    # Upper bound is the number greater than biggest polydivisible number that
                                                    # won't be reached if searching for existing polydivisible number
    while (int(number)<3610000000000000000000000):
                                                      # Checking for place where something went wrong in:
        where = isNumPoly(number)
                                                      # If 0 return number as polydivisible
        if where==0:
            return int(number)
                                                      # If not replace failing piece of the number with nicely divisible one
        badPiece=number[0:where]
        replacement = str(int(badPiece)+(where-int(badPiece)%where))
                                                      # Create new number with working first part and 0's for the rest, 
                                                      # not to skip over any number along the way
        number = replacement + "0"*len(number[where:]) 
    return None
