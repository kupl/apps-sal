def reverse_letter(string):
    gnirts = ''
    for i in range(0, len(string)):
        if string[i].isalpha():
            gnirts = string[i] + gnirts
    return gnirts
