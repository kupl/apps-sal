def gap(num):
    return len(max(bin(num)[2:].split('1')[1:-1]))
