
def nth_even(n):
    if not isinstance(n, int):
        raise TypeError("sorry, only intergers allowed - try again")
    if n < 1:
        raise ValueError("sorry, enter a number larger than 0")

    return n * 2 - 2
