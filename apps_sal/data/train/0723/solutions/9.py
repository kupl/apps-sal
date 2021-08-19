import sys
for __ in range(eval(input())):
    n = eval(input())
    (ans, const) = ('', False)
    for i in range(n):
        (p, a) = list(map(int, sys.stdin.readline().split()))
        (coeff, power) = (0, 0)
        if a > 0:
            coeff = a * p
            power = a - 1
            if power != 0:
                if n == 1:
                    ans += str(coeff) + 'x^' + str(power)
                    const = True
                else:
                    ans += str(coeff) + 'x^' + str(power) + ' + '
            else:
                ans += str(coeff)
                const = True
    print(0 if ans == '' else ans.strip() if const else ans[:len(ans) - 3].strip())
