def dont_give_me_five(start,end):
    answer = 0
    for i in range(start,end +1):
        if not("5" in str(i)):
            answer += 1
    return answer  # amount of numbers
