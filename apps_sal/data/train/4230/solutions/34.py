def reverse_letter(string):
    string = string[::-1]
    string2 = ''
    for x in range(0, len(string)):
        if string[x].isalpha():
            string2 += string[x]
    return string2
