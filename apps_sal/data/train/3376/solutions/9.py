def square_free_part(n):
    if type(n) != int or n < 1:
        return
    ans = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            ans *= i
            while n % i == 0:
                n //= i
    if n > 1:
        ans *= n
    return ans
