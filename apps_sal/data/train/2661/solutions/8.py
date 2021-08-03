from re import compile

REGEX = compile(r"^(?:https?:\/\/)?(?:\w+\.)*?codwars\.com(?:$|\/.*$|\?.*$)").fullmatch


def find_codwars(url):
    return bool(REGEX(url))
