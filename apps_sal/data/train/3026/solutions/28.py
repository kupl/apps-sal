def min_value(digits):
    dSet = sorted(set(digits))
    outStr = ""
    for i in dSet:
        outStr += str(i)
    return int(outStr)
