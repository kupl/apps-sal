def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    return [i for i in range(a, b + 1) if i == sum(int(x)**(j + 1) for j, x in enumerate(str(i)))]
