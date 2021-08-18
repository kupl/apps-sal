def correct(string):
    trans = string.maketrans({"0": "O", "1": "I", "5": "S"})
    return string.translate(trans)
