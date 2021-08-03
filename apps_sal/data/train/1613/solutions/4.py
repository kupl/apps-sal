from re import sub


def solution(string, markers):
    return sub("(.*?) ?([\%s].*)" % "\\".join(markers), "\g<1>", string) if markers else string
