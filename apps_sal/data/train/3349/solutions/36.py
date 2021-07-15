def find_missing_number(sequence):
    lst = sequence.split(" ")

    if sequence == "":
        return 0

    try:
        numbers = sorted([int(x) for x in lst])
    except ValueError:
        return 1

    if numbers == list(range(1, len(numbers)+1)):
        return 0
    
    if numbers[0] == 2 and numbers == list(range(2, len(numbers) + 2)):
        return 1

    #"It must return 1 for a sequence missing the first element"

    else:
        for i in range(len(numbers)-1):
            if numbers[i] + 1 != numbers[i+1]:
                return numbers[i] + 1
