def find_missing_number(sequence):
    if sequence == '':
        return 0
    x = sequence.split()
    result = []
    for i in x:
        if i.isdigit() == False:
            return 1
        elif i.isdigit() == True:
            result.append(int(i))
    result.sort()
    start = 0
    for i in range(len(result)):
        if result[i] == start + 1:
            start = start + 1
        else:
            prev = start
            break
    else:
        return 0
    return prev + 1
