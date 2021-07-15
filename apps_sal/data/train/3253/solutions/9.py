def womens_age(n):
    return str(n) + "? That's just 20, in base " + str(n//2) + "!" if n % 2 == 0 else str(n) + "? That's just 21, in base " + str(n//2) + "!"
