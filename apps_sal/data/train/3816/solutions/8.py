a = 'abcdefghijklmnopqrstuvwxyz'
def move_ten(st):
    return ''.join(a[(a.find(x)+10)%26] for x in st)
