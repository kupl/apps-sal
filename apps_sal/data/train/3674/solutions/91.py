def add_binary(a,b):
    decimal = a + b
    output = ''
    while decimal != 0:
        str_bin = str(decimal % 2)
        output = output + str_bin
        decimal = decimal // 2 
    return output[::-1]
