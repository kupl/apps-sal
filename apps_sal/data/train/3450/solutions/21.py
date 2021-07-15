def array(string):
    string = string.replace(" ", "")
    arr = string.split(",")
    return None if len(arr) < 3 else " ".join(arr[1:-1])
