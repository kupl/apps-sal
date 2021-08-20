def every(array, interval=0, start_index=0):
    if interval == 0:
        return array
    return [x for (ind, x) in enumerate(array[start_index:]) if ind % interval == 0]
