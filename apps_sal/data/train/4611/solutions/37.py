def animals(heads, legs):
    i = 0
    while i <= heads:
        chicken_number = i
        cow_number = heads - chicken_number
        if chicken_number * 2 + cow_number * 4 == legs:
            return (chicken_number, cow_number)
        i += 1
    return 'No solutions'
