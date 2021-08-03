# write the function is_anagram
def is_anagram(test, original):
    if len(test) > len(original) or len(test) < len(original):
        return False

    res = ''
    counter = 0
    sortedTest = sorted(test.lower())
    sortedOriginal = sorted(original.lower())

    for i in range(0, len(sortedTest)):
        if sortedTest[i] != sortedOriginal[i]:
            res = False
            break
        else:
            res = True
    return res
