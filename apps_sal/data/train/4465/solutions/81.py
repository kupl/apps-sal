def super_size(n):
    singleValues = []
    x = 1
    result = 0

    while n >= 1:
        singleValues.append(n % 10)
        print((n % 10))
        n = int(n / 10)

    singleValues.sort()
    print(singleValues)

    for i in singleValues:
        result = result + i * x
        x = x * 10

    print(result)
    return(int(result))
