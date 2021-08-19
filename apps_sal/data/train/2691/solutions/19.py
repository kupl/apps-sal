def solve(s):
    k = 0
    a = ''
    talha = []
    for i in s:
        if i.isalpha() == True:
            a = a + 'x'
        else:
            a = a + i
    b = a.split('x')
    for i in b:
        if i.isdigit() == True:
            talha.append(int(i))
    return max(talha)
