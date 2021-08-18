def sum_str(a, b):
    try:
        s = int(a) + int(b)
        return str(s)
    except:
        if(a == "" and b == ""):
            return "0"
        elif(a == ""):
            return b
        else:
            return a
