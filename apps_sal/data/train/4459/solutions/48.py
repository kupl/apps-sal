
def nth_even(n):
    #ensuring we have the right input
    if not isinstance(n, int):
         raise TypeError("sorry, only intergers allowed - try again") 
    if n <1:
        raise ValueError("sorry, enter a number larger than 0")

    #this is the formula for showing the nth even number
    return n*2-2
