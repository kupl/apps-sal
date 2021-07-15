def array_leaders(numbers):
    return [elem for idx,elem in enumerate(numbers) if elem>sum(numbers[idx+1:])]
