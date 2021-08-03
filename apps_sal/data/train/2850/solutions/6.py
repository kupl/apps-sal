def gordon(a):
    a = a.upper()
    a = a.replace(' ', '!!!! ')
    a = a.replace('A', '@')
    vowels = ['E', 'I', 'O', 'U']
    for each in vowels:
        a = a.replace(each, '*')
    return a + '!!!!'
