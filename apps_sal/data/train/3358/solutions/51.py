def correct(string):
    answer = ''
    for c in string:
        if c == '5':
            answer += 'S'
        elif c == '0':
            answer += 'O'
        elif c == '1':
            answer += 'I'
        else:
            answer += c

    return answer
