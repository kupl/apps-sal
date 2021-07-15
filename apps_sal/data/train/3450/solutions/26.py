def array(string):
    string = string.replace(' ','')
    arr = string.split(',')
    if len(arr) <= 2:
        return None
    else: 
        return ' '.join(arr[1:-1])
