def lovefunc( flower1, flower2 ):
    if all([isinstance(i, int) for i in [flower1,flower2]]):
        return not ((flower1+flower2)%2 == 0) # only the sum of odd and even can be odd, that is love:)
    else:
        print('both of the numbers must be integers!')
