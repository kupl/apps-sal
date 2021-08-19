def get_average(marks):
    # assumption array is never empty
    # get average of an array and return

    # will use sum and len of array to get average
    # rounded down to nearest integer
    avg = sum(marks) // len(marks)
    return avg

    # raise NotImplementedError("TODO: get_average")
