def solution(number):
    return sum(num if (num % 3 == 0) or (num % 5 == 0) else 0 for num in range(number))
