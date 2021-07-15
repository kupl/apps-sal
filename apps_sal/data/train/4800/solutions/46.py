def hotpo(n):
    count = 0
    num = n
    if(n < 1):
        return 1
    while(num > 1):
        if(num % 2 == 0):
            num = num / 2
        else:
            num = 3 * num + 1
        count += 1
    return count

