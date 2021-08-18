def array(string):
    string = string.replace(" ", "")
    array = string.split(",")
    array = array[1:-1]
    return " ".join(array, ) if len(array) > 0 else None
