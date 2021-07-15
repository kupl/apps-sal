def reverse_number(n):
    spacer = n < 0
    return int(['','-'][spacer] + str(n)[spacer:][::-1])
