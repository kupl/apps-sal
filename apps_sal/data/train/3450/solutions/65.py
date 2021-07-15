def array(s):
    arr = s.split(",")[1:-1]
    if arr == []:
        return None
    return " ".join(arr)
