def first_non_repeating_letter(string):
    result = sorted(string, key=lambda x: string.lower().count(x.lower())) + ['']
    return result[0] if result.count(result[0]) == 1 else result[-1]
