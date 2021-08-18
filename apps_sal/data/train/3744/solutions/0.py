def oddest(numbers):
    most_odd = 0
    max_oddity = -1
    is_unique = True
    for num in numbers:
        oddity = 0
        print(num)
        insider = num
        while insider % 2 == 1:
            if insider == -1:
                oddity = 1 + max([abs(n) for n in numbers])
                break
            else:
                oddity += 1
                insider = (insider - 1) / 2
        if oddity > max_oddity:
            is_unique = True
            max_oddity = oddity
            most_odd = num
        elif oddity == max_oddity:
            is_unique = False
    if is_unique and max_oddity >= 0:
        return most_odd
    return None
