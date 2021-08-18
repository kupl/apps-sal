def sum_dig_pow(a, b):
    return [i for i in range(a, b + 1) if i == sum(int(x)**(j + 1) for j, x in enumerate(str(i)))]
