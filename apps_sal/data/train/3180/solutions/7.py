def trotter(n):
    if not n:
        return 'INSOMNIA'
    dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    increment = n
    while True:
        for i in str(n):
            dict[int(i)] = dict.get(int(i), 0) + 1
        if next((j for j in dict.values() if j == 0), 1):
            break
        n += increment
    return n
