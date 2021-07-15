def index(array, n):
    if array==[]:
        return -1
    if len(array)>n:
        return array[n]**n
    else: return -1

