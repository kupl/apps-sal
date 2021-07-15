def min_value(digits):
    digits.sort()

    print(digits)
    i=0
    while i <= len(digits)-2:
        print(i)
        if digits[i] == digits[i+1]:
            digits.pop(i)
            
            print(digits)
        else :
            print(digits)
            i+=1
    s = ""
    for x in digits:
        s += str(x)
    return int(s)


