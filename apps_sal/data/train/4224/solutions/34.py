def dont_give_me_five(start, end):
    answer = 0
    for i in range(start, end + 1):
        if '5' in str(i):
            pass
        else:
            answer += 1
    return answer
