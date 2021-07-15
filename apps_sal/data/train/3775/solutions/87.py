def digits(n):
    digit = n
    answer = 1
    while digit >= 10:
        digit = digit /10
        answer += 1
    return answer
