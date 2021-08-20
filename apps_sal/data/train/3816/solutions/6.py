def move_ten(st):
    a = 'abcdefghijklmnopqrstuvwxyzabcdefghij'
    return ''.join([a[a.find(i) + 10] for i in st])
