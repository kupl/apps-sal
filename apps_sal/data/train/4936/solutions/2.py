def reverse(lst):
    empty_list = list()
    result = list()
    while lst:
        result.append(lst.pop())
    return result
