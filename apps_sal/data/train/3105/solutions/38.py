def count_sheep(n):
    count = 1
    message = ''
    while count <= n:
        message = message + str(count) + ' sheep...'
        count += 1
    return message
