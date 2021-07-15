def positive_sum(list):
    answer = 0
    for numbers in list: 
        if numbers > 0:
            answer += numbers
    return answer
