# My 1st Solution

def duplicate_count(text):
    count = 0
    counted = []
    test = list(text.lower())
    for i, c in enumerate(test):
        if test.count(test[i]) >= 2 and counted.count(test[i]) == 0:
            count += 1
            counted.append(test[i])
            test.remove(test[i])
    return count
