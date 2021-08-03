def first_non_repeating_letter(string):
    duplicates = [i for i in string if string.lower().count(i.lower()) == 1]
    return duplicates[0] if duplicates else ''
