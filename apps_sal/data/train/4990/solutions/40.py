def solution(string, ending):
    if len(ending) > len(string):
        return False

    out = True
    inc = 0
    revString = string[::-1]
    for i in ending[::-1]:
        if i != revString[inc]:
            out = False
        inc = inc + 1
    return out
