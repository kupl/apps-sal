def find_nth_occurrence(substring, string, occurrence=1):
    (c, i) = (1, string.find(substring))
    while c < occurrence and i > -1:
        (c, i) = (c + 1, string.find(substring, i + 1))
    return i
