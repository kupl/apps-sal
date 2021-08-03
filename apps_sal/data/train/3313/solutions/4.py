import re


def highlight(code):
    code = re.sub(r'(\d+)', r'<span style="color: orange">\1</span>',
                  re.sub(r'(R+)', r'<span style="color: green">\1</span>',
                         re.sub(r'(L+)', r'<span style="color: red">\1</span>',
                                re.sub(r'(F+)', r'<span style="color: pink">\1</span>',
                                       code))))
    return code
