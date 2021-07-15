def skiponacci(n):
    mas = []
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        mas.append(fib1)
    sas = []
    for i in range(0, len(mas), 2):
        sas.append(str(mas[i]))
    if n % 2 == 0:
        return " skip ".join(sas) + " skip"
    else:
        return " skip ".join(sas)
