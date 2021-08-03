def queue_time(customers, n):
    cajas = [0] * n
    for i in customers:
        cajas[0] += i
        cajas = sorted(cajas)
        print(cajas)
    return cajas[-1]
