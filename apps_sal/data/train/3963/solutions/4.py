def amicable_numbers(n1,n2):
    divisors1 = [i for i in range(1,n1) if n1%i==0]
    divisors2 = [i for i in range(1,n2) if n2%i==0]
    return bool(sum(divisors1)==n2 and sum(divisors2)==n1)
