import re
def validate_number(s):
    if re.match(r'^(07|\+447)+\d{9}$', s.replace('-','')):
        return 'In with a chance'
    else:
        return 'Plenty more fish in the sea'
