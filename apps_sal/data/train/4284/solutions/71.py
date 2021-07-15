def array_leaders(numbers):
    # return [numbers[i] for i in range(len(numbers)) if numbers[i] > sum(numbers[i + 1:])]
    return [n for i, n in enumerate(numbers) if n > sum(numbers[i + 1:])]



#     a = []
#     for i in range(len(numbers) - 1):
#         if numbers[i] > sum(numbers[i + 1:]): a.append(numbers[i])

# if numbers[-1] > 0: a.append(numbers[-1])
        
#     return a

