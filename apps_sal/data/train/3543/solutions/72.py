import re


def increment_string(strng):
    num = re.findall('\\d+', strng)
    if len(num) == 0:
        return strng + '1'
    else:
        num = num[-1]
        new_num = int(num) + 1
        if len(str(num)) > len(str(new_num)):
            num_zeros = len(str(num)) - len(str(new_num))
            new_strng = strng.replace(str(num), str('0' * num_zeros + str(new_num)))
        else:
            new_strng = strng.replace(str(num), str(new_num))
        return new_strng
