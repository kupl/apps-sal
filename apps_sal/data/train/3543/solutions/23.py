from re import compile

p = compile(r"(.*?)(\d*$)")


def increment_string(strng):
    s, n = p.search(strng).groups()
    return f"{s}{int(n or 0) + 1:0{len(n)}d}"
