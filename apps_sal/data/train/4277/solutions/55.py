def difference_in_ages(ages):
    x = []
    x.append(min(ages)) 
    x.append(max(ages))
    x.append(max(ages) - min(ages))
    return tuple(x)
