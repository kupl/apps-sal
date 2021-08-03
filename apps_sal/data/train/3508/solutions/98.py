def halving_sum(n):
    answer = 0
    while n > 0:
        answer += n
        n = n // 2
    return answer
