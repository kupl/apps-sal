def reverse_letter(string):
    array = list(filter(str.isalpha, string))
    new_list = ''.join(array)
    return new_list[::-1]
