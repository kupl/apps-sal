from re import search, escape


def solution(string, ending):
    return bool(search(escape(ending) + '\Z', string))
