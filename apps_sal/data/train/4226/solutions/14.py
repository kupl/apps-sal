def remove_smallest(numbers):
    if len(numbers) < 1:
        return []
    answer = numbers[:]
    minimum = min(numbers)
    answer.remove(minimum)
    return answer
