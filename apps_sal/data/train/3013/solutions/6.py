def delete_digit(n):
    max = 0
    str_n = str(n)
    for i in range(len(str_n)):
        temp = str_n[:i] + str_n[i + 1:]
        if max < int(temp):
            max = int(temp)
    return max
