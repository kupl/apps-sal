def problem(a):
    if isinstance(a, str):
        return 'Error'
    else:
        answer = a * 50
        answer += 6
        return answer
