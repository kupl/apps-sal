from collections import defaultdict

def duplicates(lst):
    result = []
    counter = defaultdict(int)
    for elem in lst:
        counter[elem] += 1
        if counter[elem] == 2:
            result.append(elem)
    return result
