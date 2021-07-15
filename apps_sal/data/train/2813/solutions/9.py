def switcher(arr):
    return ''.join({'27':'!','28':'?','29':' '}.get(i, chr(123 - int(i))) for i in arr)
