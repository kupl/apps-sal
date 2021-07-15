def sum_triangular_numbers(n):
    step = 0
    triangulars = [0]
    while n > len(triangulars)-1:
        step += 1
        triangulars.append(triangulars[-1] + step)
    return sum(triangulars)

