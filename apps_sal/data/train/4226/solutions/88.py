def remove_smallest(numbers):
    if len(numbers) > 0 :
        newList = []
        sortedList = sorted(numbers)
        popped = sortedList.pop(0)
        newList = numbers[:]
        newList.remove(popped)
        return newList
    else:
        return []
