import re


def words_to_object(s):
    matches = re.findall(r'(.+?)\s(.+?)\s', s + ' ')
    return "[" + ", ".join(["{{name : '{}', id : '{}'}}".format(x[0], x[1]) for x in matches]) + "]"
