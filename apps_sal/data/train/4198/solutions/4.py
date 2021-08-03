from math import sqrt


def simplify(n):
    li = [i for i in range(2, n) if n % i == 0 and sqrt(i) == int(sqrt(i))]
    return (f"{int(sqrt(li[-1]))} sqrt {n // li[-1]}" if li else f"sqrt {n}") if sqrt(n) != int(sqrt(n)) else f"{int(sqrt(n))}"


def desimplify(s):
    s = s.split()
    try:
        return int(pow(int(s[0]), 2)) * (int(s[-1]) if len(s) > 1 else 1)
    except:
        return int(s[1])
