def find(n):
    num = 0
    if n % 5 == 0 or n % 3 == 0:
        num += n
    for i in range(3, n):
        if not i % 5 or not i % 3:
            num = num + i
    return num
