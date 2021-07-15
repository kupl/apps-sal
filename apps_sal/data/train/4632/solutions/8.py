def decode(string):
    dict = {"1":"9", "2":"8", "3":"7","4":"6","5":"0","6":"4", "7":"3","8":"2","9":"1","0":"5"}
    return "".join([dict[x] for x in string])
