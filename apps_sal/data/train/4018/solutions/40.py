def isDigit(string):
    #x = ["-"]
    # if string.isnumeric() ==True:
    # return True
    # elif char

    # return string.isnumeric()
    try:
        float(string)
        return True
    except ValueError:
        return False
