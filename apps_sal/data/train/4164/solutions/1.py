from collections import Counter
def first_non_repeating_letter(string):
    cnt = Counter(string.lower())
    for letter in string:
        if cnt[letter.lower()] == 1:
            return letter
    return ''
