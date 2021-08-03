def is_uppercase(inp):
    count = 0
    my_inp = inp.replace(' ', '')
    for i in my_inp:
        if i.isupper() and i.isalpha():
            count += 1
        elif not i.isalpha():
            count += 1
    if count == len(my_inp):
        return True
    return False
