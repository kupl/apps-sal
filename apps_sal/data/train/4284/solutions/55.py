def array_leaders(numbers):
    return [k for i,k in enumerate(numbers) if sum(numbers[i+1:]) < k]
