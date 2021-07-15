def count_letters_and_digits(s):
    count = 0
    for x in s:
        if x.isalpha() or x.isnumeric():
            count += 1
    return count
