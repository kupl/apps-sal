import re


def highlight(code):
    code = re.sub('(\\d+)', '<span style="color: orange">\\1</span>', re.sub('(R+)', '<span style="color: green">\\1</span>', re.sub('(L+)', '<span style="color: red">\\1</span>', re.sub('(F+)', '<span style="color: pink">\\1</span>', code))))
    return code
