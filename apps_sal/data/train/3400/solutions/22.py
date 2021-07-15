def even_numbers(array, requiredResultLength):
    return [number for number in array if not number % 2][-requiredResultLength:]
