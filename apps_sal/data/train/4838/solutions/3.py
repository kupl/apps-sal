def find_nth_occurrence(substring, string, occurrence=1):
    i = -1
    for _ in range(occurrence):
        i = string.find(substring, i + 1)
        if i == -1:
            break
    return i
