def mem_alloc(banks):
    seen = set()
    while tuple(banks) not in seen:
        seen.add(tuple(banks[:]))
        num = max(banks)
        i = banks.index(num)
        banks[i] = 0
        while num:
            i = (i + 1) % len(banks)
            banks[i] += 1
            num -= 1
    return len(seen)

