import re


def meeting(s):
    return "".join(
        sorted(
            re.sub("(\w+):(\w+);?", r"(\2, \1);", s.upper())
            .split(";")
        )
    )
