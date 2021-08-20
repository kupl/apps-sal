def correct(string):
    answer = ''
    for i in string:
        if i == '0':
            answer += 'O'
        elif i == '5':
            answer += 'S'
        elif i == '1':
            answer += 'I'
        else:
            answer += i
    return answer
