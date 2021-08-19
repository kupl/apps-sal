def reverse_number(n):
    ans = 0
    if n >= 0:
        while n > 0:
            ans *= 10
            ans += n % 10
            n = n // 10
        print(ans)
        return ans
    elif n < 0:
        n = n * -1
        while n > 0:
            ans *= 10
            ans += n % 10
            n = n // 10
        print(ans)
        return ans * -1
