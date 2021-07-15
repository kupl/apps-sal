memo = {}
def factorial(n):
    if n in memo.keys():
        return memo[n]
    elif n == 0:
        return 1
    else:
        ans = n*factorial(n-1)
        memo[n] = ans
    return ans
def strong_num(number):
    play = str(number)
    add = 0
    for num in play:
        add += factorial(int(num))
    if add == number:
        return "STRONG!!!!"
    return "Not Strong !!"
