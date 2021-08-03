def multi_table(number):
    string = ''
    for i in range(1, 11):
        string += (f"{i} * {number} = {i * number}\n")
    string = string[:-1]
    return(string)
