def animals(heads, legs):
    print((heads, legs))
    if heads == 0 and legs == 0:
        return (0, 0)
    elif heads <= 0 or legs <= 0:
        return "No solutions"
    else:
        if legs % 4 == 0 and legs / 4 == heads:
            return (0, heads)
        elif legs % 2 == 0 and legs / 2 == heads:
            return (heads, 0)
        else:
            cow_try = legs / 4
            chicken = (heads - cow_try) * 2
            cow = heads - chicken
            if cow // 1 + chicken // 1 == heads and cow > 0 and chicken > 0:
                return (chicken, cow)
            else:
                return "No solutions"
        

