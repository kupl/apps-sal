def sum_cubes(n):
    answer = 0
    for i in range(n+1):
        answer += i ** 3
    return answer
