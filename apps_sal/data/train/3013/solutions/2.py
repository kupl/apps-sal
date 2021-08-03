def delete_digit(n):
    for z in range(len(str(n)) - 1):
        if int(str(n)[z]) < int(str(n)[z + 1]):
            return int(str(n)[:z] + str(n)[z + 1:])
    return int(str(n)[:-1])
