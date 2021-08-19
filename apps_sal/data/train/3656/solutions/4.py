def decompose(n):
    if '/' in n:
        strs = n.split('/')
        a = int(strs[0])
        b = int(strs[1])
    elif '.' in n:
        strs = n.split('.')
        b = 10 ** len(strs[1])
        a = int(strs[1]) + b * int(strs[0])
    else:
        a = int(n)
        b = 1
    output = []
    while a >= b:
        i = a // b
        a = a - b * i
        output.append(str(i))
    while a > 0:
        i = b // a + 1 if b % a else b // a
        a = a * i - b
        b = b * i
        output.append('1/' + str(i))
    return output
