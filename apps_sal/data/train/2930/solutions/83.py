def summation(num):

    result = 0
    count = 1

    while count <= num:
        result += count
        count += 1

    return result


def __starting_point():
    assert summation (4)
    

__starting_point()
