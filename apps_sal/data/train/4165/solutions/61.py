def uni_total(string):
    try:
        return sum([ord(i) for i in string])
    except:
        return 0
