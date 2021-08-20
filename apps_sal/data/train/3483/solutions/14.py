def string_parse(string):
    if type(string) != str:
        return 'Please enter a valid string'
    try:
        out = string[:2]
        temp = ''
        for i in string[2:]:
            if i == out[-1] == out[-2]:
                temp += i
            else:
                if temp != '':
                    out += '[' + temp + ']'
                out += i
                temp = ''
        if temp != '':
            out += '[' + temp + ']'
        return out
    except:
        return 'Please enter a valid string'
