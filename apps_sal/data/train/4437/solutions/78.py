def cookie(x):
    result = "Who ate the last cookie? It was "
    if isinstance(x, str):
        result += "Zach"
    elif (isinstance(x, int) or isinstance(x, float)) and not isinstance(x, bool):
        result += "Monica"
    else:
        result += "the dog"
    result += "!"
    return result
