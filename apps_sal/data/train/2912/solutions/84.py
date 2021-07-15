def find_multiples(integer, limit):
    print(integer, limit)
    answer = [integer]
    while answer[-1] + integer <= limit:
        answer.append(answer[-1] + integer)
    return answer
