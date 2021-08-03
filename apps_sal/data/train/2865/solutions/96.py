def solution(string):

    if len(string) == 0:
        return ""
    else:
        li = []
        for i in range(len(string) - 1, -1, -1):
            li.append(string[i])

        sort = "".join(li)
        return sort
