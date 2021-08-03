def correct(string):
    dict = {"5": "S", "0": "O", "1": "I"}
    str = ""
    for x in string:
        if x in dict:
            str += dict[x]
        else:
            str += x
    return(str)
