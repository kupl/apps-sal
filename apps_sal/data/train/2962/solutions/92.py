def divisible_by(numbers, divisor):
    wf = [] 
    dhf = [numbers, divisor]
    for i in numbers:
        if (i / divisor) == (i // divisor):
            wf.append(i)
    return wf
