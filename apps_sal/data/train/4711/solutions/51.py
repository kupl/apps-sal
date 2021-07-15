def zeros(n):
    answer = 0
    i = n
    while i > 0:
        i //= 5
        answer += i
    return answer
