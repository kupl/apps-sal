def row_sum_odd_numbers(n):
    triangle = []
    odd = 1
    for row in range(n):
        triangle.append([])
        while len(triangle[row]) < row + 1:
            triangle[row].append(odd)
            odd += 2
    return (sum(triangle[n - 1]))
