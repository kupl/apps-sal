def compound_array(a, b):
    answer = []
    while a or b:
        if a:
            answer.append(a.pop(0))
        if b:
            answer.append(b.pop(0))
    return answer
