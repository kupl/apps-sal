def balanced_num(number):
    numbers_array = [int(num) for num in str(number)]
    if len(numbers_array) % 2: 
        del numbers_array[int(len(numbers_array) // 2 + 0.5)]  
    else:
        del numbers_array[len(numbers_array) // 2 - 1 : len(numbers_array) // 2 + 1]

    return 'Balanced' if sum(numbers_array[:len(numbers_array)//2]) == sum(numbers_array[len(numbers_array)//2:]) else 'Not Balanced'
