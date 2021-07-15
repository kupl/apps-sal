def digits(n):
    answer = 0
    while n != 0:
        n = n // 10
        answer += 1
    return answer
