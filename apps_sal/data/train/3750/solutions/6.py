def count_letters_and_digits(s):
    return len([item for item in s if item.isalpha() or item.isdigit()])
