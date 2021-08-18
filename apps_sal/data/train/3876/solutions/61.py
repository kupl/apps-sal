def find(n):
    holder = 0
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0:
            holder = holder + i
    return holder
