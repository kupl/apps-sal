def count_letters_and_digits(s):
    numerics = 0
    letters = 0
    other = 0
    for i in s:
        if i.isnumeric():
            numerics += 1
        elif i.isalpha():
            letters += 1
        else:
            other += 1
    return numerics + letters
