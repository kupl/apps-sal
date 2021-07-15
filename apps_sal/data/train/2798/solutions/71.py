def to_alternating_case(string):
    resultStr = ""
    for k in string:
        if k.islower():
            resultStr += k.upper()
        elif k.isupper():
            resultStr += k.lower()
        else: 
            resultStr += k
    return resultStr
