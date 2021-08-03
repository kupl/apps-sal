def correct(string):
    dict = {"5": "S", "0": "O", "1": "I"}
    new = ""
    for i in string:
        if i in dict.keys():
            new += dict[i]
        else:
            new += i
    return new
