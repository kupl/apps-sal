from math import sqrt


def is_smooth(n):
    smooth = {2: "power of 2",
              3: "3-smooth",
              5: "Hamming number",
              7: "humble number"}

    s = set()
    i = 2
    while i <= sqrt(n):
        while n % i == 0:
            s.add(i)
            n //= i
        i += 1
    s.add(n)

    return smooth.get(max(s), "non-smooth")
