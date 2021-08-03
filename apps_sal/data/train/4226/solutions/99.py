def remove_smallest(numbers):
    answer_numbers = numbers[:]
    if numbers != []:
        answer_numbers.remove(min(answer_numbers))
        return answer_numbers
    else:
        return numbers
