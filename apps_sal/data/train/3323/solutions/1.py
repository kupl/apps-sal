def faulty_odometer(n):
    result = 0
    digits = len(str(n))
    nonaryTranslation = "".join([str(int(x)-1) if int(x) >= 5 else x for x in list(str(n))])
    for i in nonaryTranslation:
        digits -= 1
        result += int(i) * (9**digits)
    return result
    

