def to_alternating_case(string):
    answer = ''
    for i in range(len(string)):
        if string[i].islower():
            answer += string[i].upper()
        else:
            answer += string[i].lower()
    return answer
