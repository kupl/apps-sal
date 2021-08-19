def solution(string):
    # use the built-in list as a stack
    res = ''
    flip = list(string)

    # while the stack has elements
    while len(flip) > 0:
        # pop and append to result
        res += flip.pop()

    return res
