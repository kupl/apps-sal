def withdraw(n):
    bills = [0, 0, 0]
    print(n)
    if n >= 100:
        while n >= 100:
            if n == 130 or n == 110:
                break
            n -= 100
            bills[0] += 1
    if n == 50 or n == 70 or n == 90 or n == 130 or n == 110:
        while n >= 50:
            if n == 80:
                break
            if bills[1] == 1:
                break
            n -= 50
            bills[1] += 1
    if n > 0:
        while n > 0:
            n -= 20
            bills[2] += 1
    
    return bills

