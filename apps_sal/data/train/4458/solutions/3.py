from typing import Union
from re import compile

r = compile(r"(\d\d):(\d\d):(\d\d)")


def time_correct(t: Union[str, None]) -> Union[str, None]:
    if not t:
        return t

    f = r.fullmatch(t)
    if f:
        h, m, s = list(map(int, f.groups()))
        h, m = divmod(h * 3600 + m * 60 + s, 3600)
        m, s = divmod(m, 60)

        return f"{h % 24:02}:{m:02}:{s:02}"
