def repeat_it(string, n):
    if type(string) == str:
        return string * n
    else:
        return 'Not a string'


print(repeat_it(1234, 2))
