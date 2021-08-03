def my_first_kata(a, b):
    if isinstance(a, bool) or isinstance(b, bool):
        return False
    if isinstance(a, int) and isinstance(b, int):
        #print (a,b)
        return (a % b) + (b % a)
    return False
