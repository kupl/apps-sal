from re import compile

r = compile(r"79(?=7)")


def seven_ate9(s: str) -> str:
    return r.sub("7", s)
