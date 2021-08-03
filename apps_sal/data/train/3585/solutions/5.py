def proc_seq(*args):
    result = []
    mems = []
    numbers = [""]
    for a in args:
        mems.append(list(set(str(a))))

    nnumbers = []
    for a in mems:
        nnumbers = list(map(lambda x: (list(map(lambda y: y + x, numbers))), a))
        numbers = []
        for a in nnumbers:
            for b in a:
                numbers.append(b)

    numbers = list(filter(lambda x: x[0] != '0', numbers))

    numbers = list(map(lambda x: int(x), numbers))
    numbers.sort()

    if(len(numbers) == 1):
        return [len(numbers), sum(numbers)]
    return [len(numbers), numbers[0], numbers[len(numbers) - 1], sum(numbers)]
