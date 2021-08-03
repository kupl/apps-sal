def sum_triangular_numbers(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        cont = 0
        num = 1
        max = 2
        result = 1

        while(max <= n):
            num += 1
            cont += 1
            if cont == max:
                result += num
                max += 1
                cont = 0
        return result
