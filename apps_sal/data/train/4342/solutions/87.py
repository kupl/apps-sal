def no_space(x):
    answer = ''
    for i in x:
        if i == ' ':
            continue
        else:
            answer += i
    return answer
