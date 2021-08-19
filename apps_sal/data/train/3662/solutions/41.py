def xor(a, b):
    a = [a]
    b = [b]
    # if (sum(a+b) ==0) or (sum(a+b) == 2):
    #   return False
    # else:
    #   return True
    return (sum(a + b) == 1)
