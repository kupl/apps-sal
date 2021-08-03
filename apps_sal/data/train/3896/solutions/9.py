def solution(number):
    multiples = []
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)
    for x in multiples:
        sum += x
    return(sum)
