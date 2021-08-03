from re import compile

REGEX = compile(r"(\d{2}):(\d{2}):(\d{2})").search


def time_correct(t):
    if not t:
        return t
    try:
        H, M, S = map(int, REGEX(t).groups())
        q, S = divmod(S, 60)
        q, M = divmod(M + q, 60)
        H = (H + q) % 24
        return f"{H:02}:{M:02}:{S:02}"
    except AttributeError:
        pass
