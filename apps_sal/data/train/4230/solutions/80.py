def reverse_letter(string):
    result = list(string[::-1])
    answer = []
    for i in result:
        if i.isalpha():
            answer.append(i)
    return ''.join(answer)
