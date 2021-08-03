def mix_fruit(arr):
    regular = ["banana", "orange", "apple", "lemon", "grapes"]
    special = ["avocado", "strawberry", "mango"]
    return round(sum(5 if fruit.lower() in regular else (7 if fruit.lower() in special else 9) for fruit in arr) / len(arr))
