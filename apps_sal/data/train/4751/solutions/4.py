def sum_of_divisors(number):
    divisors = [1]
    i = 2
    while i < number//i:
        if not number%i:
            divisors.append(i)
            divisors.append(number//i)
        i += 1
    if i**2==number: divisors.append(i)
    return sum(divisors)

def is_perfect(number):
    return number == sum_of_divisors(number)

def is_amicable(number_1, number_2):
    return number_2 == sum_of_divisors(number_1)
    
def deficiently_abundant_amicable_numbers(n1,n2):
    perfect_1 = "perfect" if is_perfect(n1) else False
    if not perfect_1: perfect_1 = "abundant" if n1 < sum_of_divisors(n1) else "deficient"
    perfect_2 = "perfect" if is_perfect(n2) else False
    if not perfect_2: perfect_2 = "abundant" if n2 < sum_of_divisors(n2) else "deficient"
    amicable = "amicable" if is_amicable(n1,n2) and not (is_perfect(n1) and is_perfect(n2)) else "not amicable"
    return perfect_1 + " " + perfect_2 + " " + amicable
