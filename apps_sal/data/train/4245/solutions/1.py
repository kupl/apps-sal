def explode(arr):
    numbers = [n for n in arr if type(n) == int]
    return [arr] * sum(numbers) if numbers else "Void!"
