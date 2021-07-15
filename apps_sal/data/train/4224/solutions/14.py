dont_give_me_five = lambda s,e: len([i for i in range(s, e+1) if '5' not in str(i)])
#loops through each number in start, end, converting each number to a string and checking if '5' is contained within, if it isn't present, it is added to a list, the length of the list is calculated and returned as the result.

