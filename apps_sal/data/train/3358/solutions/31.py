def correct(string):
#     return string.replace("0", "O").replace("1", "I").replace("5", "S")
    trans = string.maketrans({"0":"O", "1":"I", "5":"S"})
    return string.translate(trans)
