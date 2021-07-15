def difference_in_ages(ages):
    ages.sort()
    a=ages[0]
    b=ages[-1]
    m=b-a
    return(a,b,m)
