def solution(string):

    lst = []
    count = 1

    for i in range(0, len(string)):

        lst.append(string[len(string) - count])
        count += 1

    lst = ''.join(lst)
    return lst
