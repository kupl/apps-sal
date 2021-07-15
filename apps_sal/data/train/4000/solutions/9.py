def strong_num(number):
    result = []
    for i in str(number):
        fact = 1
        for j in range(1, int(i) + 1):
            fact = fact * j
        result.append(fact)
    return "STRONG!!!!" if sum(result) == number else "Not Strong !!"
