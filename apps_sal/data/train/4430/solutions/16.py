import re


def vowel_2_index(string):
    pattern = re.compile(r'([aeiouAEIOU])')
    for i in re.finditer(pattern, string):
        s = str(i.start() + 1)
        string = string.replace(i.group(), s, 1)
    return string
