def find_nth_occurrence(substring, string, occurrence=1):
    index = -1
    for occ in range(0, occurrence):
        index = string.find(substring, index + 1)
    return index
