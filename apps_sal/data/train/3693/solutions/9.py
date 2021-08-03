def make_negative(number):
    if "-" in str(number):
        return(number)
    else:
        return int("-" + str(number))
