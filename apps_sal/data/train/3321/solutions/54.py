def evil(n):
    binary = bin(n)[2:]

    count = 0
    for i in str(binary):
        if i == '1':
            count += 1
    
    if count % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"

