
def reverse(lst):
    empty_list = list()            # use this!
    result = list()
    while lst:
        result.append(lst.pop())
    return result

