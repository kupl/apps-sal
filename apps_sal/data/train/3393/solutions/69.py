def factors(n):
    return set([f for i in range(1, int(n**0.5)+1) if n % i == 0 for f in [i, n//i]])

def list_squared(m, n):
    ans = []
    for i in range(m, n):
        sum_of_squares = sum(map(lambda x: x**2, factors(i)))
        if (sum_of_squares ** 0.5) % 1 == 0:
            ans.append([i, sum_of_squares])
    return ans
