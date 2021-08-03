def bubblesort_once(l):
    values = l[:]
    for i in range(0, len(values) - 1):
        first = values[i]
        second = values[i + 1]
        if(first > second):
            values[i + 1] = first
            values[i] = second
    return values
