def mem_alloc(banks):
    seen = set()
    while tuple(banks) not in seen:
        seen.add(tuple(banks))
        number = max(banks)
        index = banks.index(number)
        banks[index] = 0
        while number:
            index = (index + 1) % 16
            banks[index] += 1
            number -= 1
    return len(seen)
