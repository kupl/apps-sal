def reverse_letter(string):
    lst = ''.join([i for i in string if i.isalpha()])
    rev = lst[::-1]
    return rev
