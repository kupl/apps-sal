def max_number(n):
    leList = []
    for ele in str(n):
        leList.append(int(ele))
    leList.sort(reverse=True)
    return int(''.join((str(f'{x}') for x in leList)))
