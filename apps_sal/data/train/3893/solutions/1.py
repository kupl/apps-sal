def divisors(integer):
    a = []
    for i in range(2, integer):
        if integer % i == 0:
            a.append(i)
    return a if a else str(integer) + " is prime"
