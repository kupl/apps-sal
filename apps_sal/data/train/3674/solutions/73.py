def add_binary(n1, n2):
    n = n1 + n2

    def decToBin(num):
        if num == 0:
            return ''
        else:
            return decToBin(num // 2) + str(num % 2)
    if n == 0:
        return 0
    else:
        return decToBin(n)
