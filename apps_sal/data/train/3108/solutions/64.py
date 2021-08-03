def multi_table(number):
    lst = list()
    for i in range(1, 11):
        result = f"{i} * {number} = {i*int(number)}"
        lst.append(result)
    return "\n".join(lst)
