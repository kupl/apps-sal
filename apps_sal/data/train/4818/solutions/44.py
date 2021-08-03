def solution(a, b):
    short, int = '', ''
    if len(a) > len(b):
        long = a
        short = b
    else:
        short = a
        long = b

    return short + int + short
