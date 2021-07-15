def reverse_letter(string):
    arr = list(filter(str.isalpha, string))
    arr.reverse()
    return ''.join(arr)

