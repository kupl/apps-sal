
import functools

def compares(item1, item2):
    if len(item1) == 0:
        return -1
    if len(item2) == 0:
        return 1
    if ord(item1[0].lower()) < ord(item2[0].lower()):
        return -1
    elif ord(item1[0].lower()) > ord(item2[0].lower()):
        return 1
    else:
        return compares(item1[1:], item2[1:])

def compare(item1, item2):
    return compares(item1,item2)
def sorter(textbooks):
    #Cramming before a test can't be that bad?
    return sorted(textbooks, key=functools.cmp_to_key(compare))

