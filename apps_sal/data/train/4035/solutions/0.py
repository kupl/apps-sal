def substring_test(first, second):
    first = first.lower()
    second = second.lower()

    for i in range(len(first) - 2):
        if first[i:i+2] in second:
            return True
    return False
