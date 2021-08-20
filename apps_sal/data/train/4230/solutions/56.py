def reverse_letter(string):
    result = ''
    for i in range(1, len(string) + 1):
        if string[-i].isalpha():
            result += string[-i]
    return result
