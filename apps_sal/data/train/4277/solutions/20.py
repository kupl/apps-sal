def difference_in_ages(ages):
    # your code here
    age = sorted(ages)
    age_len = len(age)
    young = age[0]
    old = age[age_len - 1]
    diff = old - young
    result = (young, old, diff)
    return result
