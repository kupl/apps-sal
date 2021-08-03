def even_numbers(arr, n):
    arr = arr[::-1]
    solution = []
    for i in arr:
        if i % 2 == 0:
            solution.append(i)
            if len(solution) == n:
                solution = solution[::-1]
                return solution
