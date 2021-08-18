def opposite(number):
    numbers = str(number)
    if isinstance(number, int):
        if numbers[0] == "-":
            negatives = numbers[1:]
            negative = int(negatives)
            return negative
        else:
            positives = "-" + numbers
            positive = int(positives)
            return positive
    if isinstance(number, float):
        if numbers[0] == "-":
            negatives = numbers[1:]
            negative = float(negatives)
            return negative
        else:
            positives = "-" + numbers
            positive = float(positives)
            return positive
