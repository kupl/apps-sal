def evil(n):
    num = bin(n)
    ones = 0 
    for i in num:
        if i == '1':
            ones += 1
    return "It's Evil!" if ones % 2 == 0 else "It's Odious!"
