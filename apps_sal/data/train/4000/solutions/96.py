fact = [1]
for i in range(1, 10):
    fact.append(i * fact[i-1])

def strong_num(number):
    total = 0
    tmp = number
    while tmp > 0:
        total += fact[tmp % 10]
        tmp = int(tmp / 10)
    if total == number:
        return "STRONG!!!!"
    return "Not Strong !!"

