def solution(string):
    i = -1

    backwards = []

    # loop through and add the letters backwards to a list
    while i >= -1 * len(string):
        backwards.append(string[i])
        i -= 1
    # return the list all joined back into a string
    return(''.join(backwards))
