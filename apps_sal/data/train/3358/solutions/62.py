def correct(string):
    d = {"5":"S","1":"I","0":"O"}
    new = ""
    for i in string:
        if i.isalpha():
            new+=i
        elif i=="5" or i=="0" or i=="1":
            new+= d[i]
        else:
            new+=i
    return new
