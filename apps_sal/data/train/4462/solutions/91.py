
def adjacent_element_product(array):
    i = 0
    listy = []
    while i < (len(array) - 1):
        num = int(array[i]) * int(array[i + 1])
        listy.append(num)
        i += 1

    return max(listy)
