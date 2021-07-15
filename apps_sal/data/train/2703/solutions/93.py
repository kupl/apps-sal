def square_sum(numbers):
    final_answer = 0
    for number in numbers:
        square = number ** 2
        final_answer += square
    return final_answer
