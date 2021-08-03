dict = {"5": "S", "0": "O", "1": "I"}


def correct(string):
    for i in string:
        if i in dict.keys():
            string = string.replace(i, dict[i])
    return string
