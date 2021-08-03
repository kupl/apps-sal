def solution(string, ending):
    l = len(ending)
    l = 0 - l
    if string[l:] == ending or ending == '':
        ans = True
    else:
        ans = False
    return ans
