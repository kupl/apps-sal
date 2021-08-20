import re
rx = re.compile('(?<=7)9(?=7)')


def seven_ate9(str_):
    return rx.sub('', str_)
