def sum_cubes(n):
    (cubes, numbers) = ([], [n])
    for i in range(0, n):
        numbers.append(int(i))
    for num in numbers:
        cubes.append(int(num * num * num))
    return sum(cubes)
