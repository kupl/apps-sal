
def reverse_letter(string):
    result = ''.join([i for i in string if not i.isdigit()])
    alphanumeric = ''.join([i for i in result if i.isalnum()])

    return alphanumeric[::-1]
