import re


def increment_string(string):
    if string:
        num = []
        word = ''
        for i, s in enumerate(string[::-1]):
            if re.findall('\d', s):
                num.insert(0, s)
                i = i + 1
            else:
                break
        if i > len(string) - 1:
            pass
        else:
            j = i
            while j < len(string):
                word = word + string[j - i]
                j = j + 1
        if num:
            return word + str(int(''.join(num)) + 1).zfill(len(num))
        else:
            return word + '1'
    else:
        return '1'
