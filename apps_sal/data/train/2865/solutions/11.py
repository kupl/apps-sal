def solution(string):
    charlist = []
    res = ""
    for l in string:
        charlist.append(l)
    charlist.reverse()
    for c in charlist:
        res = res + c
    return res
