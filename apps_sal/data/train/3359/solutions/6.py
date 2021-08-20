from string import ascii_uppercase as letters


def title_to_number(title):
    transfer = list(title)[::-1]
    result = 0
    for (i, char) in enumerate(transfer):
        result += (letters.find(char) + 1) * 26 ** i
    return result
