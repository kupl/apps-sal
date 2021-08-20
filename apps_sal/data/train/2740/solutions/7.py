def wheat_from_chaff(values):
    results = values[:]
    head = 0
    tail = len(values) - 1
    while True:
        while results[head] <= 0 and head < tail:
            head += 1
        while results[tail] > 0 and tail > head:
            tail -= 1
        if head >= tail:
            break
        (results[head], results[tail]) = (results[tail], results[head])
    return results
