def pattern(n): return "\n".join(["".join([" "] * (n - 1) + [str(i % 10)] * n + [" "] * (n - 1)) for i in range(1, n)] + ["".join([str(x % 10) for x in range(1, n)] + [str(n % 10)] * n + [str(x % 10) for x in range(n - 1, 0, -1)]) for i in range(n)] + ["".join([" "] * (n - 1) + [str(i % 10)] * n + [" "] * (n - 1)) for i in range(n - 1, 0, -1)])

# and if you are reading this after having completed it without plenty of
# list comprehensions, you know you should feel ashamed, z3rocoo1 :(
# Kore wa joku desu; ganbatte, kohai ;)
