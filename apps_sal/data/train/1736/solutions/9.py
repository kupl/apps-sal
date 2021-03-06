def is_interesting(number, awesome_phrases, within=2):
    if number in awesome_phrases:
        return 2
    if number >= 100:
        n = str(number)
        if set(n[1:]) == {'0'}:
            return 2
        if len(set(n)) == 1:
            return 2
        if n in '1234567890':
            return 2
        if n in '9876543210':
            return 2
        if n == n[::-1]:
            return 2
    return any((is_interesting(number + i + 1, awesome_phrases, 0) for i in range(within)))
