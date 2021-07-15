def reverse_letter(string):
    answer = []
    for a in string[::-1]:
        if a.isalpha() == True:
            answer.append(a)
    return ''.join(answer)
