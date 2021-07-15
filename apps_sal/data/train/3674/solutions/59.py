def add_binary(a,b):
    'Add two numbers'
    add = a + b
    'Convert the sum to binary (excluding the two first characters) and then convert into a string'
    return str(int(bin(add)[2:]))

