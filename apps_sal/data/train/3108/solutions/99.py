def multi_table(number):
    result = ''
    for i in range(1, 11):
        if i == 10:
            result += f"{i} * {number} = {i * number}"
        else:
            result += f"{i} * {number} = {i * number}\n"
    return result
