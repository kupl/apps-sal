def find_nth_occurrence(substring, string, occurrence=1):
    indicies = [i for i in range(len(string)) if string.startswith(substring, i)]
    if occurrence > len(indicies):
        return -1
    else:
        return indicies[occurrence - 1]

