def amicable_numbers(n1,n2):
    return sum(d for d in range(1,n1//2 + 1) if not n1 % d) == n2 and sum(d for d in range(1,n2//2 + 1) if not n2 % d) == n1
