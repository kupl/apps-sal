def find_nth_occurrence(substring, string, occurrence):
    a = string.find(substring)
    while a >= 0 and occurrence > 1:
        a = string.find(substring, a + 1)
        occurrence -= 1
    return a
