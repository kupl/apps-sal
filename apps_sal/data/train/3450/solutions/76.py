def array(string):
    string = string.replace(" ", "")
    array = string.split(",")
    array = array[1:-1]
    return " ".join(array, ) if len(array) > 0 else None
#string[2:-2] if len(string) > 4 else None
