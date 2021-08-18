from re import compile

count = compile(r"[a - zA - Z][ | }; &
auto=compile(r"(?i)automatik").search
mecha=compile(r"(?i)mechanik").search


def count_robots(a):
    x=y=0
    for s in a:
        if auto(s):
            x += len(count(s))
        elif mecha(s):
            y += len(count(s))
    return [f"{x} robots functioning automatik", f"{y} robots dancing mechanik"]
