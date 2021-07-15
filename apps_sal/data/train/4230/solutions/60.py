def reverse_letter(string):
    ls = list(string)
    reverse = ls.reverse()
    reversed_cleaned = ''
    for i in range(len(ls)):
        if ls[i].isalpha():
            reversed_cleaned += ls[i]
    return reversed_cleaned

