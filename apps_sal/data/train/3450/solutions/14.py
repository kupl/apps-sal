def array(string):
    string = string.split(',')
    print(len(string))
    print(string)
    if len(string) <= 2:
        return None
    else:
        string = string[1:-1]
        print(string)
        return ' '.join(string)
