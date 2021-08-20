def to_alternating_case(string):
    answer = ''
    for c in string:
        if c.isupper():
            answer += c.lower()
        elif c.islower():
            answer += c.upper()
        else:
            answer += c
    return answer
