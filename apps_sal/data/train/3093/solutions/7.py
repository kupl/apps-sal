from itertools import groupby

is_odd = set("13579").__contains__


def insert_dash(num: int) -> str:
    return ''.join(('-' if k else '').join(g) for k, g in groupby(str(num), key=is_odd))

