import re


def highlight(code):
    code = re.sub('(F+)', '<span style="color: pink">\\g<1></span>', code)
    code = re.sub('(L+)', '<span style="color: red">\\g<1></span>', code)
    code = re.sub('(R+)', '<span style="color: green">\\g<1></span>', code)
    code = re.sub('(\\d+)', '<span style="color: orange">\\g<1></span>', code)
    return code
