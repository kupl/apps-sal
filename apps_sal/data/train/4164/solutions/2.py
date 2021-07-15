def first_non_repeating_letter(string):
    singles = [i for i in string if string.lower().count(i.lower()) == 1]
    return singles[0] if singles else ''
