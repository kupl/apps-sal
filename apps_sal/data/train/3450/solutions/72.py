def array(s):
    arr = s.replace(' ', '').split(',')
    return None if len(arr) <= 2 else ' '.join(arr[1:-1])
