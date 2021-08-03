def variance(li):
    common = 1 / len(li)
    e_of_x = sum(len(i) * common for i in li)
    result = sum((len(i) ** 2) * common for i in li) - e_of_x ** 2
    return round(result, 4)
