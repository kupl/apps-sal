def seven_ate9(str_):
    txt = ''
    print(str_)
    for (index, letter) in enumerate(str_):
        if index == 0 or index + 1 == len(str_):
            txt += letter
            continue
        elif str_[index - 1] == '7' and str_[index + 1] == '7' and (letter is '9'):
            continue
        txt += letter
    return txt
