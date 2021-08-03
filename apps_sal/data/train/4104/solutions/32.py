def max_tri_sum(numbers):
    answer = []
    numbers.sort(reverse=True)
    for MaxNumbers in numbers:
        if MaxNumbers not in answer and len(answer) < 3:
            answer.append(MaxNumbers)
        elif answer == 3:
            break
        print(answer)
    return(sum(answer))
