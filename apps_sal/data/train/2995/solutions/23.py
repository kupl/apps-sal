def sum_mul(n, m):
    answer = 0
    if n > 0 and m > 0:
        for i in range(n, m, n):
            answer += i
        return answer
    else:
        return 'INVALID'
