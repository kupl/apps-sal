def is_isogram(string):
    s = set(string.lower()) 
    if len(s) == len(string): 
        return True
    return False
