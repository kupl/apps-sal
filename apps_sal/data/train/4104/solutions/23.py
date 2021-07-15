def max_tri_sum(numbers):
    count = 0
    answer = 0
    numbers = set(numbers)
    while count < 3:
        answer += max(numbers)
        numbers.remove(max(numbers))
        count += 1
    return answer
