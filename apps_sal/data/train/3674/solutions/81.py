def add_binary(a, b):
    # your code here

    num = a + b
    binary = ''
    while num > 0:
        val = num % 2
        binary += str(val)
        num = num // 2

    return(binary[::-1])
