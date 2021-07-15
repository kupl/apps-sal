def solution(number):
    a = (number - 1) // 5
    b = (number - 1) // 3
    c = (number - 1) // 15
    
    sum_a = ((a * (a + 1)) // 2) * 5
    sum_b = ((b * (b + 1)) // 2) * 3
    sum_c = ((c * (c + 1)) // 2) * 15
    
    return sum_a + sum_b - sum_c
