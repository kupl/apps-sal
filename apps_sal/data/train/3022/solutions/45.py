def two_highest(arg1):
    #set() to get unique values
    #sorted() to sort from top to bottom
    #slice [:2] to pick top 2
    return(sorted(set(arg1),reverse=True)[:2])
