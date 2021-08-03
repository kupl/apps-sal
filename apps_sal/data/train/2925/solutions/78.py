def multiply(n):
    c = 0
    for i in str(n):
        for j in i:
            if j.isdigit():
                c += 1
    five = 1
    while c != 0:
        c -= 1
        five *= 5
    return five * n
