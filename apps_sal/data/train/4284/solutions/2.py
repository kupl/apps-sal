def array_leaders(numbers):
    return [j for i,j in enumerate(numbers) if j > sum(numbers[i+1:]) ]
