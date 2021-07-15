def find_multiples(integer, limit):
    answer = []
    i = 0
    number = integer
    while number <= limit:
        i = number
        answer.append(i)
        number += integer
    return answer
