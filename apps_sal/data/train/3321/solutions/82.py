def evil(n):
    binary = bin(n).replace("0b", "")
    count = 0
    for i in str(binary):
        if i == '1':
            count = count + 1
    if count % 2 == 0:
        return "It's Evil!"
    return "It's Odious!"
