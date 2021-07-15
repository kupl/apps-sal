def uni_total(string):
    result=0
    print(string)
    for i in string:
        print(ord(i))
        result=result+ord(i)
    return result
