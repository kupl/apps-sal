def multi_table(number):
    l = [f"{i} * {number} = {number*i}\n" for i in range(1,11)]
    return ''.join(l).rstrip("\n")
