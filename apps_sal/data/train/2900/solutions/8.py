def string_transformer(s):

    array = []

    if s is '':
        return ''
        
    for i in s:
        if i == i.lower():
            array.append(i.upper())
        else:
            array.append(i.lower())
            
    result = ''.join(array)
    return ' '.join(result.split(' ')[::-1])
