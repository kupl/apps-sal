from re import compile

r = compile(r"(\W)")


def reverser(sentence: str) -> str:
    return ''.join(w[::-1] for w in r.split(sentence))
