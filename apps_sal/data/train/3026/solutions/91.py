def min_value(digits):
    min = ""
    dig2 = list(dict.fromkeys(digits))
    dig2.sort()
    for i in dig2:
        min = min+str(i)
    return int(min)

