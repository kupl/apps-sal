def balanced_num(number):
    s,l=str(number),len(str(number))
    return "Balanced" if sum([int(x) for x in s[:(l-1)//2]])==sum([int(x) for x in s[l//2+1:]]) else "Not Balanced"
