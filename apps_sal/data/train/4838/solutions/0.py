def find_nth_occurrence(substring, string, occurrence=1):
    idx = -1
    for i in range(occurrence):
        idx = string.find(substring, idx + 1)
        if idx == -1: return -1
    return idx
