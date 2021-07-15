def remove_smallest(numbers):
    new = []
    for i in numbers:
        new.append(i)
    try:
        new.remove(min(new))
        return new
    except:
        return []

