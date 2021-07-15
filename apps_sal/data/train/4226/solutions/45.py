def remove_smallest(numbers):
    num = numbers.copy()
    if len(numbers) < 1 :
        return  num

    else:
        num.remove(min(num))
        return num

