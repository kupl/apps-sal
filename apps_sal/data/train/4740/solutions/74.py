def row_sum_odd_numbers(n):
    digits_counter = sum(range(n+1))
    triangle_content = []
    while len(triangle_content) != digits_counter:
        for i in range(digits_counter * 2 + 1):
            if i % 2 == 1:
                triangle_content.append(i)
    final_sum = 0
    for digit in triangle_content[len(triangle_content) - n:]:
        final_sum += digit
    return final_sum
