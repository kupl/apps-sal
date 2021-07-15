def seven_ate9(string):
    answ = []
    for i, item in enumerate(string):
        if i == 0 or i == len(string)-1:
            answ.append(item)
        elif item == '9':
            if string[i-1] == '7' and string[i+1] == '7':
                continue
            else:
                answ.append(item)
        else:
            answ.append(item)
    return ''.join(answ)
