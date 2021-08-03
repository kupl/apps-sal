import re


def time_correct(s):
    try:
        assert re.match(r"^\d\d:\d\d:\d\d$", s)
        a, b, c = [int(x) for x in s.split(":")]
    except:
        return "" if s == "" else None
    b += c // 60
    a += b // 60
    return ":".join("{:>02}".format(x % y) for x, y in zip([a, b, c], [24, 60, 60]))
