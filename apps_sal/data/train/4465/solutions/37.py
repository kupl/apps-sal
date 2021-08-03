def super_size(n):
    bigest = ""
    amount = len(str(n))
    numbers = []
    n = str(n)
    for i in range(amount):
        numbers.append(n[i])
    numbers.sort(reverse=True)
    for i in range(amount):
        bigest += numbers[i]
    bigest = int(bigest)
    return(bigest)
