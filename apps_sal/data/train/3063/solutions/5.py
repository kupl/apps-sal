def mix_fruit(arr):
    arr = [x.lower() for x in arr]
    total = 0
    total_number_of_fruits = len(arr)
    for fruit in arr:
        if fruit in ['banana', 'orange', 'apple', 'lemon', 'grapes']:
            total += 5
        elif fruit in ['avocado', 'strawberry', 'mango']:
            total += 7
        else:
            total += 9

    answer = round(total / total_number_of_fruits)
    return answer
