def reverse_letter(string):
    outputArray = []
    for a in string:
        if a.isalpha():
            outputArray.append(a)
    outputArray.reverse()
    return ''.join(outputArray)
