def divisible_by(numbers, divisorr):
    a = []
    for i in numbers:
        if i % divisorr == 0:
            a.append(i)
    return a
        

