def correct(string):
    d = []
    for i in string:
        if i == "5":
            d.append("S")
        elif i == "0":
            d.append("O")  
        elif i == "1":
            d.append("I")  
        else:
            d.append(i)
    return "".join(d)      
