def find(number):
    result = []
    for i in range(1, number+1):
        if i % 3 == 0 or i % 5 == 0:
            result.append(i)

    return sum(result)
