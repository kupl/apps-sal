import re


def increment_string(strng):
    digits_regex = '\\d+$'
    value_regex = '[1-9]+$'
    ret_str = ''
    digits_match = re.search(digits_regex, strng)
    if digits_match:
        digits = digits_match.group(0)
        print(digits)
        substr = strng[0:strng.index(digits)]
        ret_str += substr
        value_match = re.search(value_regex, digits)
        if value_match:
            value = value_match.group(0)
            print(value)
            leading_zeros = digits[0:digits.rfind(value)]
            if value.count('9') == len(value):
                leading_zeros = leading_zeros[0:-1]
            ret_str += leading_zeros
            value = str(int(value) + 1)
            ret_str += value
        else:
            digits = digits[0:-1] + '1'
            ret_str += digits
    else:
        ret_str = strng + '1'
    return ret_str
