def sharkovsky(a, b):
    power_a, odd_number_a = solve(a)
    power_b, odd_number_b = solve(b)
    print(("a info power then oddnum", power_a, odd_number_a))
    if(odd_number_a == 1 and odd_number_b == 1):
        return True if power_a > power_b else False
    elif(odd_number_a == 1 and odd_number_b > 1):
        return False
    elif(odd_number_a > 1 and odd_number_b == 1):
        return True
    elif(power_a > power_b):
        return False
    elif(power_a < power_b):
        return True
    elif(power_a == power_b):
        return True if odd_number_a < odd_number_b else False


def solve(a):
    power_of_two = 0
    num = a
    while num % 2 == 0:
        power_of_two += 1
        num = num / 2
    return power_of_two, a / (2 ** power_of_two)
