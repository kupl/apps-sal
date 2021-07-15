def is_anagram(test, original):
    l1 = list(test.lower())
    l2 = list(original.lower())
    if len(l1) == len(l2):
        for i in l1:
            if i in l2:
                l2.remove(i)
            else:
                return False
    else:
        return False
    return True
