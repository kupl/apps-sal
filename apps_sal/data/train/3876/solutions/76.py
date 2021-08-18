def find(n):
    i = 1
    count = 0
    while i <= n:

        if (i % 3) == 0 or (i % 5) == 0:
            count = count + i
        i = i + 1
    return (count)
