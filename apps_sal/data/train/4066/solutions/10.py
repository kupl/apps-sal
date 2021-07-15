def string_to_array(s):
    arr = []
    
    words = s.split(" ")
    if len(s) == 0:
        return [""]
    
    for word in words:
        arr.append(word)
    
    return arr
