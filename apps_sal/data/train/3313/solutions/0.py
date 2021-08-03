import re


def highlight(code):
    code = re.sub(r"(F+)", '<span style="color: pink">\g<1></span>', code)
    code = re.sub(r"(L+)", '<span style="color: red">\g<1></span>', code)
    code = re.sub(r"(R+)", '<span style="color: green">\g<1></span>', code)
    code = re.sub(r"(\d+)", '<span style="color: orange">\g<1></span>', code)
    return code
