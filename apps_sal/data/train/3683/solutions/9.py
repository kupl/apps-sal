def letter_count(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
