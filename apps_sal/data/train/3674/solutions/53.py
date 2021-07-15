def add_binary(a,b):
    num = a+b
    temp = bin(num)
    index = 0
    binary = ""
    for i in temp:
        if index != 0 and index != 1:
            binary += i
        index += 1
    return binary

