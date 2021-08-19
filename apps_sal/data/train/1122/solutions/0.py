while True:
    try:
        m = int(input())
        n = int(m / 2)
        a = m - n
        sum_even = int(2 * (2 * n * (n + 1) * (2 * n + 1)) / 3)
        sum_odd = int((4 * a * a * a - a) / 3)
        result = sum_odd + sum_even
        if result % 2 == 0:
            print('Ravi')
        else:
            print('Jhon')
    except:
        break
