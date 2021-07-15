import re

def validate_code(code):
    return bool(re.match(r'^[1-3]',str(code)))

# easy non-regex solution would be the following
#
# def validate_code(code):
#     return list(str(code))[0] in list('123')

