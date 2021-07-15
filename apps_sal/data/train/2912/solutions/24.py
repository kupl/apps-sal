def find_multiples(integer, limit):
    n = integer
    answer = []
    while n <= limit:
        answer.append(n)
        n += integer
    return answer
