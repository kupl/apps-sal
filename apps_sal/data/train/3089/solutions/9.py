def dashatize(num):
    if type(num) != int:
        return 'None'
    a = ['-{}-'.format(x) if int(x) % 2 != 0 else '{}'.format(x) for x in list(str(num).strip("-"))]

    return "".join(a).strip("-").replace("--", "-")
