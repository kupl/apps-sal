def palindrome_chain_length(n):
    step = 0
    while True:
        r = reverse(n)
        if n == r:
            break
        n += r
        step += 1
    return step


def reverse(n):
    ans = 0
    while n > 0:
        ans = 10 * ans + n % 10
        n //= 10
    return ans
