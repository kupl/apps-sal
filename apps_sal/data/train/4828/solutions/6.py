def count_squareable(n):
    count = 0
    for number in range(1 , n+1):
        if number % 4 == 2:
            count += 1
    return n - count
