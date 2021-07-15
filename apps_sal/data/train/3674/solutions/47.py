def add_binary(a,b):
    c = a+b
    binary = ""
    while (c > 1): 
      binary = binary + str(c % 2)
      c = (c // 2) 
    binary = binary[::-1]
    binary = str(c) + binary
    return binary


