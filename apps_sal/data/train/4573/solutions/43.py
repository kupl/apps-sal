def over_the_road(address, n):
    biggest_num = n * 2
    lowest_num = 1
    if address % 2 > 0:
        step = address - lowest_num
        result = biggest_num - step
        return result
    else:
        step = biggest_num - address
        result = lowest_num + step
        return result
