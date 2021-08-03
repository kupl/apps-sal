def solution(a, b):
    lena = len(a)
    lenb = len(b)
    if lena > lenb:
        long = a
        short = b
    elif lena < lenb:
        long = b
        short = a
    answer = short + int + short
    return answer
