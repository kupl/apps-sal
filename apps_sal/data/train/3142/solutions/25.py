def seven_ate9(str):
    new = []
    for i, v in enumerate(str):
        if i == len(str) - 1:
            new.append(v)

        elif v == '9' and str[i - 1] == '7' and str[i + 1] == '7':
            pass

        else:
            new.append(v)
    return ''.join(new)
