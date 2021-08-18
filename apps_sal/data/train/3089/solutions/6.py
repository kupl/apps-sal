import re


def dashatize(num):
    if num == None:
        return "None"
    if num < 0:
        num = num * -1

    return "-".join(list(filter(None, re.split("(1|3|5|7|9)", str(num)))))
