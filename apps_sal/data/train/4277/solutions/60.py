def difference_in_ages(ages):
    s = sorted(ages)[0]
    s1 = sorted(ages,reverse=True)[0]
    return (s,s1,s1-s)
