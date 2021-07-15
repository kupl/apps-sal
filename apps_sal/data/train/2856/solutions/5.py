def gap(num):
    return len(max(bin(num)[2:].strip("0").split("1")))
    

