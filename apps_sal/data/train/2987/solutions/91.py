def is_divide_by(number, a, b):
    if number % a == 0 and number % b == 0:
        answer = True
    else:
        answer = False
    print(answer)
    return answer
