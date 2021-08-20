def seven_ate9(str_):
    ls = [x for x in str_]
    counter = 1
    while counter < len(ls) - 1:
        if ls[counter] == '9' and ls[counter - 1] == '7' and (ls[counter + 1] == '7'):
            ls.pop(counter)
        counter += 1
    return ''.join(ls)
